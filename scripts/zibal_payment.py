import json
import os
from typing import Any, Dict, Optional
import requests


class Zibal:
    """
    A class to interact with the Zibal payment gateway.

    Attributes:
        _payment_request_url (str): The URL for initiating payment requests.
        _payment_verify_url (str): The URL for verifying payments.
        _payment_page_url (str): The URL for the payment page.
        _callback_url (str): The callback URL after payment.
        merchant_id (Optional[str]): The merchant ID for authentication.
    """

    _payment_request_url: str = "https://gateway.zibal.ir/v1/request"
    _payment_verify_url: str = "https://gateway.zibal.ir/v1/verify"
    _payment_page_url: str = "https://gateway.zibal.ir/start/"
    _callback_url: str = "https://webhook.site/ac93c06c-9dc8-4898-bed6-57927995f661"
    merchant_id: Optional[str] = os.environ.get(
        "ZIBAL_PAYMENT_MERCHANT_ID")  # Use "zibal" for sandbox mode or retrieve from environment variables for production.

    def __init__(self, merchant_id: Optional[str] = None) -> None:
        """
        Initializes the Zibal class with a merchant ID.

        Args:
            merchant_id (Optional[str]): The merchant ID used for Zibal's API.
        """
        if merchant_id:
            self.merchant_id = merchant_id

    def payment_request(self, amount: int, description: str = "پرداختی کاربر") -> Dict[str, Any]:
        """
        Sends a payment request to Zibal and returns the response.

        Args:
            amount (int): The amount to be paid in Rials.
            description (str, optional): Description for the payment. Defaults to "پرداختی کاربر".

        Returns:
            Dict[str, Any]: A dictionary containing the response from the payment request.
        """
        payload: Dict[str, Any] = {
            "merchant": self.merchant_id,
            "amount": str(amount),
            "callbackUrl": self._callback_url,
            "description": description,
        }
        headers: Dict[str, str] = {"Content-Type": "application/json"}

        response = requests.post(
            self._payment_request_url, headers=headers, data=json.dumps(payload)
        )
        response.raise_for_status()
        return response.json()

    def payment_verify(self, track_id: str) -> Dict[str, Any]:
        """
        Verifies a payment with Zibal using the track ID.

        Args:
            track_id (str): The tracking ID of the payment.

        Returns:
            Dict[str, Any]: A dictionary containing the verification response.
        """
        payload: Dict[str, str] = {"merchant": self.merchant_id, "trackId": track_id}
        headers: Dict[str, str] = {"Content-Type": "application/json"}

        response = requests.post(
            self._payment_verify_url, headers=headers, data=json.dumps(payload)
        )
        response.raise_for_status()
        return response.json()

    def generate_payment_url(self, track_id: str) -> str:
        """
        Generates a payment URL using the track ID.

        Args:
            track_id (str): The tracking ID of the payment.

        Returns:
            str: The complete payment URL.
        """
        return f"{self._payment_page_url}{track_id}"


if __name__ == "__main__":
    zibal = Zibal(merchant_id="zibal")

    # Request payment
    response = zibal.payment_request(amount=15000)
    print(response)

    # Generate payment URL
    input("Proceed to generating payment URL?")
    payment_url = zibal.generate_payment_url(track_id=response["trackId"])
    print(payment_url)

    # Verify payment
    input("Check the payment?")
    verification_response = zibal.payment_verify(track_id=response["trackId"])
    print(verification_response)
