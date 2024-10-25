# API Reference for Zibal Payment Package

This document serves as a comprehensive reference for the available classes, methods, and exceptions in the **Zibal Payment** package. It is designed to help developers effectively utilize the package for integrating Zibal's payment services.

## Classes

### `ZibalClient`

The primary class for interacting with the Zibal API. This class handles all operations related to payment requests and verifications.

#### Initialization

```python
ZibalClient(
    merchant_id: str,
    timeout: Union[int, float] = 10,
    sandbox: bool = True,
    enable_logging: bool = True
)
```

- **Parameters**:
  - **`merchant_id`** (str): The unique identifier assigned to your Zibal account.
  - **`timeout`** (Union[int, float], optional): The maximum time (in seconds) to wait for a response from the Zibal API. Default is `10` seconds.
  - **`sandbox`** (bool, optional): Set to `True` to enable sandbox mode for testing transactions without real money. Default is `True`.
  - **`enable_logging`** (bool, optional): Enables logging of API requests and responses for debugging purposes. Default is `True`.

#### Methods

- **`payment_request(amount: int, callback_url: str, description: str) -> Dict[str, Any]`**
  - Initiates a payment request to Zibal's payment gateway.
  - **Parameters**:
    - `amount` (int): The amount to be charged, expressed in Rials.
    - `callback_url` (str): The URL to which users will be redirected after payment completion.
    - `description` (str): A brief description of the payment purpose.
  - **Returns**: A dictionary containing Zibal’s response data, including the `trackId`, which is used for tracking the payment status.

- **`payment_verify(track_id: str) -> Dict[str, Any]`**
  - Verifies the status of a payment using the provided `track_id`.
  - **Parameters**:
    - `track_id` (str): The unique identifier for the payment transaction.
  - **Returns**: A dictionary containing the verification status and additional information about the transaction.

- **`generate_payment_url(track_id: str) -> str`**
  - Generates a user-friendly payment URL for a given `track_id`, directing users to Zibal's payment page.
  - **Parameters**:
    - `track_id` (str): The track ID of the payment transaction.
  - **Returns**: A string representing the generated payment URL.

---

## Exceptions

### `ZibalError`

An exception raised when the Zibal API encounters an error. This exception helps to manage errors effectively within your application.

#### Initialization

```python
ZibalError(message: str)
```

- **Parameters**:
  - **`message`** (str): A descriptive message that details the nature of the error encountered during API interaction.

---

## Conclusion

This API reference outlines the core components and functionalities of the **Zibal Payment** package, including the initiation of payment requests, transaction verification, and error handling. For practical examples and further guidance, please refer to the [usage documentation](usage.md).

By leveraging this API reference, developers can integrate Zibal's payment services into their applications with confidence, ensuring a smooth and secure payment processing experience.

---