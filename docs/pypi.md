# Zibal Payment

**Zibal Payment** is a Python package designed to easily integrate Zibal’s online payment gateway into Django applications, providing a smooth setup process and efficient handling of payment requests, URL generation, and transaction verification. 

## Key Features

- **Quick Integration**: Seamlessly integrate Zibal’s payment gateway into Django projects with minimal configuration.
- **Complete Payment Lifecycle**: Supports all steps of the payment process, from request creation to transaction verification.
- **Sandbox Mode**: Enables safe testing in a controlled environment without real transactions.
- **Secure and Reliable**: Built with robust measures to ensure transaction data security and reliability.

---

## Installation

First, ensure that Django is installed (version 3.0 or higher is required):

```bash
pip install django>=3.0
```

Install the zibal_payment package from PyPI:

```bash
pip install zibal-payment
```

---

## Getting Started

Follow these steps to configure and use zibal_payment in your Django projects.

### 1. Initializing the Client

To initialize the `ZibalClient`, provide your Zibal `merchant_id`. This client is essential for interacting with Zibal’s payment services.

```python
from zibal_payment.client import ZibalClient

# Initialize ZibalClient with your merchant ID for handling payment requests
client = ZibalClient(merchant_id="your_merchant_id", sandbox=True)
```

#### Parameters
- **`merchant_id` (str)**: Your Zibal merchant ID.
- **`sandbox` (bool, optional)**: Set to `True` for testing purposes. Defaults to `True`.
- **`timeout` (int or float, optional)**: The maximum time (in seconds) to wait for Zibal's response. Defaults to `10` seconds.
- **`enable_logging` (bool, optional)**: Enables logging for debugging purposes. Defaults to `True`.

### 2. Creating a Payment Request

To initiate a payment request, use the `payment_request` method, specifying the `amount`, `callback_url`, and `description`. This method returns essential transaction information, including a `trackId`.

```python
try:
    response = client.payment_request(
        amount=1000,  # Amount in Rials
        callback_url="https://example.com/callback",  # URL to redirect users after payment
        description="Order #123"  # Payment description
    )
    track_id = response.get("trackId")
    print(f"Payment request successful. Track ID: {track_id}")

except ZibalError as e:
    print(f"Payment request error: {e}")
```

#### Parameters
- **`amount` (int)**: Amount in Rials.
- **`callback_url` (str)**: URL where users will be redirected post-payment.
- **`description` (str)**: Description of the payment (e.g., order details).

#### Returns
A dictionary containing `trackId` and `result`. Track ID is necessary for generating a payment URL or verifying the transaction.

### 3. Generating a Payment URL

With the obtained `trackId`, you can generate a user-friendly URL for redirecting users to Zibal’s payment page.

```python
payment_url = client.generate_payment_url(track_id)
print(f"Payment URL: {payment_url}")
```

#### Returns
- **URL** (str): The complete URL for the user to make a payment on Zibal’s gateway.

### 4. Verifying a Payment

After users complete the payment, use `payment_verify` to confirm the transaction with Zibal using the `trackId`.

```python
try:
    verification_response = client.payment_verify(track_id=track_id)
    print("Payment verification successful:", verification_response)

except ZibalError as e:
    print(f"Verification error: {e}")
```

#### Parameters
- **`track_id` (str)**: Track ID of the transaction to verify.

#### Returns
A dictionary containing verification details, including `result`, `amount`, and other transaction data.

### Example Workflow

Here's a quick workflow example to illustrate how these functions can be combined:

```python
from zibal_payment.client import ZibalClient

client = ZibalClient(merchant_id="your_merchant_id")

try:
    # Step 1: Create a payment request
    response = client.payment_request(
        amount=1000,
        callback_url="https://example.com/callback",
        description="Test Payment"
    )
    track_id = response.get("trackId")
    
    # Step 2: Generate the payment URL
    payment_url = client.generate_payment_url(track_id)
    print(f"Direct user to this URL for payment: {payment_url}")

    # Step 3: After payment, verify the transaction
    verification = client.payment_verify(track_id)
    print("Payment verification details:", verification)

except ZibalError as e:
    print(f"An error occurred: {e}")
```

---

## API Reference

For complete details on methods, parameters, and error handling, please refer to the [API Documentation](https://github.com/Mohammad222PR/zibal_payment/docs/api_reference.md).

---

## Contributions and Support

We welcome community contributions! To report issues, request features, or contribute to this project, please visit our [GitHub repository](https://github.com/Mohammad222PR/zibal_payment). 

For further instructions on advanced usage and troubleshooting, see the [Usage Guide](https://github.com/Mohammad222PR/zibal_payment/docs/usage.md).

---

