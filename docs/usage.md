### `usage.md`

# Usage of Zibal Payment Package

This document provides detailed instructions on how to use the Zibal Payment package in your Python applications.

## Getting Started

### 1. Initialization

To start using the Zibal Payment package, initialize an instance of `ZibalClient` (or `ZibalDjangoClient` if you’re working within Django) with your merchant ID. You can also specify `sandbox`, `timeout`, and `enable_logging` options.

```python
from zibal_payment.client import ZibalClient

client = ZibalClient(merchant_id="your_merchant_id")
```

### 2. Making a Payment Request

You can send a payment request using the `payment_request` method. Here’s an example:

```python
response = client.payment_request(
    amount=1000,
    callback_url="https://example.com/callback",
    description="Payment for order #12345"
)

track_id = response.get('trackId')
print(f"Track ID: {track_id}")
```

### 3. Generating a Payment URL

After receiving the `track_id`, generate a payment URL:

```python
payment_url = client.generate_payment_url(track_id)
print(f"Payment URL: {payment_url}")
```

### 4. Verifying a Payment

To verify a completed payment, use the `payment_verify` method:

```python
verification_response = client.payment_verify(track_id=track_id)
print("Verification response:", verification_response)
```

### 5. Handling Errors

Make sure to handle potential errors during payment requests or verifications by catching `ZibalError` exceptions:

```python
from zibal_payment.exceptions import ZibalError

try:
    response = client.payment_request(...)
except ZibalError as e:
    print(f"Error occurred: {e}")
```

## Conclusion

This package provides an efficient way to integrate Zibal payments into your application. For additional details, please refer to the API reference section.