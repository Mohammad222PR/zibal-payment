import json
import requests
from django.conf import settings
from typing import Dict, Any, Union
from zibal_payment.exceptions import ZibalError

class ZibalClient:
    def __init__(self, merchant_id: str, timeout: Union[int, float] = 10, sandbox: bool = True,
                 enable_logging: bool = True):
        """
        Initializes the ZibalClient with given parameters.

        Args:
            merchant_id (str): The merchant ID for Zibal.
            timeout (Union[int, float], optional): The request timeout in seconds. Defaults to 10 seconds.
            sandbox (bool, optional): Whether to use the sandbox environment. Defaults to True.
            enable_logging (bool, optional): Whether to enable logging or not. Defaults to True.
        """
        self.merchant_id = merchant_id
        self.sandbox = sandbox
        self.timeout = timeout
        self.enable_logging = enable_logging
        self.base_url = "https://gateway.zibal.ir/v1/"

        self._log(f"ZibalClient initialized with merchant_id: {self.merchant_id}, sandbox: {self.sandbox}")

    def payment_request(self, amount: int, callback_url: str, description: str) -> Dict[str, Any]:
        """
        Sends a payment request to Zibal.

        Args:
            amount (int): The amount in Rials.
            callback_url (str): The callback URL after payment.
            description (str): A brief description of the payment.

        Returns:
            Dict[str, Any]: The response data from Zibal.
        """
        url = self.base_url + "request"
        payload = self._create_payload(amount, callback_url, description)
        headers = self._create_headers()

        self._log(f"Sending payment request to {url} with payload: {payload}")

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=self.timeout)
            response.raise_for_status()

        except requests.Timeout:
            self._log("Request timed out during the payment request", error=True)
            raise ZibalError("Request timed out during the payment request")

        except requests.RequestException as e:
            self._log(f"Network error occurred: {str(e)}", error=True)
            raise ZibalError("Network error occurred during the payment request")

        data = response.json()
        self._log(f"Received response from Zibal: {data}")

        if data['result'] != 100:
            self._log(f"Payment request failed: {data['message']}", error=True)
            raise ZibalError(f"Payment request failed: {data['message']}")

        return data

    def payment_verify(self, track_id: str) -> Dict[str, Any]:
        """
        Verifies the payment with the given track ID.

        Args:
            track_id (str): The track ID for verification.

        Returns:
            Dict[str, Any]: The verification response.
        """
        url = self.base_url + "verify"
        payload = {"merchant": self.merchant_id, "trackId": track_id}
        headers = self._create_headers()

        self._log(f"Sending payment verification request to {url} with trackId: {track_id}")

        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=self.timeout)
        response.raise_for_status()

        data = response.json()
        self._log(f"Received verification response from Zibal: {data}")

        if data['result'] != 100:
            self._log(f"Payment verification failed: {data['message']}", error=True)
            raise ZibalError(f"An error occurred during the payment verification: {data['message']}")

        return data

    def generate_payment_url(self, track_id: str) -> str:
        """
        Generates a payment URL based on the track ID.

        Args:
            track_id (str): The track ID for the payment.

        Returns:
            str: The payment URL.
        """
        payment_url = f"https://gateway.zibal.ir/start/{track_id}"
        self._log(f"Generated payment URL: {payment_url}")
        return payment_url

    # ---------- Private Methods ----------

    def _create_headers(self) -> Dict[str, str]:
        """Creates the necessary headers for requests."""
        return {"Content-Type": "application/json"}

    def _create_payload(self, amount: int, callback_url: str, description: str) -> Dict[str, Any]:
        """Creates the payload for payment request."""
        return {
            "merchant": self.merchant_id,
            "amount": str(amount),
            "callbackUrl": callback_url,
            "description": description,
        }

    def _log(self, message: str, error: bool = False) -> None:
        """Logs messages if logging is enabled."""
        if self.enable_logging:
            print(f"ERROR: {message}" if error else message)


class ZibalDjangoClient(ZibalClient):
    def __init__(self):
        """
        Initializes ZibalDjango with settings from Django's settings.py file.
        """
        merchant_id = settings.ZIBAL_MERCHANT_ID
        sandbox = getattr(settings, 'ZIBAL_SANDBOX', True)
        timeout = getattr(settings, 'ZIBAL_TIMEOUT', 10)
        enable_logging = getattr(settings, 'ZIBAL_ENABLE_LOGGING', True)

        super().__init__(merchant_id=merchant_id, timeout=timeout, sandbox=sandbox, enable_logging=enable_logging)
