
### `api_reference.md`

# API Reference for Zibal Payment Package

This document provides a detailed reference for the classes and methods available in the Zibal Payment package.

## Classes

### `ZibalClient`

The main class for interacting with the Zibal API.

#### Initialization

```python
ZibalClient(merchant_id: str, timeout: Union[int, float] = 10, sandbox: bool = True, enable_logging: bool = True)
```

- **merchant_id**: The merchant ID for Zibal.
- **timeout**: The request timeout in seconds (default is 10).
- **sandbox**: Whether to use the sandbox environment (default is True).
- **enable_logging**: Whether to enable logging (default is True).

#### Methods

- **`payment_request(amount: int, callback_url: str, description: str) -> Dict[str, Any]`**
  - Sends a payment request to Zibal.
  - **Parameters**:
    - `amount`: The amount in Rials.
    - `callback_url`: The callback URL after payment.
    - `description`: A brief description of the payment.
  - **Returns**: A dictionary with the response data.

- **`payment_verify(track_id: str) -> Dict[str, Any]`**
  - Verifies the payment with the given track ID.
  - **Parameters**:
    - `track_id`: The track ID for verification.
  - **Returns**: A dictionary with the verification response.

- **`generate_payment_url(track_id: str) -> str`**
  - Generates a payment URL based on the track ID.
  - **Parameters**:
    - `track_id`: The track ID for the payment.
  - **Returns**: The payment URL as a string.

## Exceptions

### `ZibalError`

Raised when there is an error with the Zibal API requests.

#### Initialization

```python
ZibalError(message: str)
```

- **message**: The error message to be displayed.

## Conclusion

This API reference provides the necessary details to use the Zibal Payment package effectively. For more examples and usage details, refer to the usage documentation.
```