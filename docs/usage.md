
### `usage.md`

# Usage of Zibal Payment Package

This document provides instructions on how to use the Zibal Payment package effectively in your Python applications.

## Getting Started

### 1. Initialization

To start using the Zibal Payment package, you need to create an instance of `ZibalDjangoClient` (or `ZibalClient` if you prefer) with your merchant ID.

```python
from zibal_payment.client import ZibalDjangoClient

client = ZibalDjangoClient()
```

### 2. Making a Payment Request

You can send a payment request by calling the `payment_request` method. Here’s an example:

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

Once you have the `track_id`, you can generate a payment URL:

```python
payment_url = client.generate_payment_url(track_id)
print(f"Payment URL: {payment_url}")
```

### 4. Verifying a Payment

To verify a payment, use the `payment_verify` method:

```python
verification_response = client.payment_verify(track_id=track_id)
print("Verification response:", verification_response)
```

### 5. Handling Errors

Make sure to handle exceptions when making payment requests or verifications. Use the `ZibalError` exception to catch any errors:

```python
from zibal_payment.exceptions import ZibalError

try:
    response = client.payment_request(...)
except ZibalError as e:
    print(f"Error occurred: {e}")
```

## Conclusion

With this package, integrating Zibal payments into your application is straightforward and efficient. For further assistance, refer to the API reference section.
