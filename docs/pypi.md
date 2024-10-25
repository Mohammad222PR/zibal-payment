Certainly! Here’s a more detailed description for your PyPI page:

---

# zibal_payment

`zibal_payment` is a comprehensive and secure Python package crafted specifically for integrating Zibal’s online payment gateway into Django applications. This package simplifies payment processing tasks, including creating payment requests, generating payment URLs, and verifying completed transactions with Zibal’s services.

![GitHub Stars](https://img.shields.io/github/stars/Mohammad222PR/zibal-payment?style=flat-square) ![GitHub Forks](https://img.shields.io/github/forks/Mohammad222PR/zibal-payment?style=flat-square) ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square) ![MIT License](https://img.shields.io/github/license/Mohammad222PR/zibal-payment?style=flat-square)

## Key Features

- **Simple Integration**: Quickly integrate Zibal’s payment gateway into Django projects with minimal setup.
- **Full Payment Lifecycle Support**: Handle all steps of the payment process, from creating payment requests to verifying transactions.
- **Sandbox Mode**: Ideal for testing payment flows in a controlled environment without real transactions.
- **Secure and Reliable**: Built to ensure the security and integrity of transaction data.

## Installation

Install the package from PyPI:

```bash
pip install zibal-payment
```

## Getting Started

Below is a basic guide on using the package in Django projects.

### 1. Initializing the Client

By default, `ZibalDjangoClient` is the primary client for Django integrations. Just initialize it with your Zibal merchant ID.

```python
from zibal_payment.client import ZibalDjangoClient

# Initialize the ZibalDjangoClient for handling payment requests with default settings
client = ZibalDjangoClient()

```

### 2. Creating a Payment Request

Use the `payment_request` method to create a payment request. Specify essential details such as the amount, callback URL, and a description.

```python
try:
    response = client.payment_request(
        amount=1000,  # Amount in Rials
        callback_url="https://example.com/callback",  # Callback URL for the response
        description="Order #123"
    )
    track_id = response.get("trackId")
    print(f"Payment request successful. Track ID: {track_id}")

except ZibalError as e:
    print(f"Payment request error: {e}")
```

### 3. Generating a Payment URL

Once you have a `track_id`, generate a user-friendly URL to direct customers to the Zibal payment page.

```python
payment_url = client.generate_payment_url(track_id)
print(f"Payment URL: {payment_url}")
```

### 4. Verifying a Payment

After customers complete their payment, verify it using the `payment_verify` method to confirm the transaction's success.

```python
try:
    verification_response = client.payment_verify(track_id=track_id)
    print("Payment verification successful:", verification_response)

except ZibalError as e:
    print(f"Verification error: {e}")
```

## API Reference

For a complete list of methods, parameters, and error handling strategies, see the full [API Reference](https://github.com/Mohammad222PR/zibal-payment/blob/main/docs/api_refrence).

## Contributions and Support

Contributions are welcome to further enhance this package’s functionality. For reporting issues or suggesting improvements, visit the [GitHub repository](https://github.com/Mohammad222PR/zibal_payment). Additionally, refer to the [Usage Guide](https://github.com/Mohammad222PR/zibal-payment/blob/main/docs/usage.md) for more in-depth instructions on integrating the package into your projects.



