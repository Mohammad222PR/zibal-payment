---

# **Zibal Payment Gateway Integration**

![GitHub Stars](https://img.shields.io/github/stars/Mohammad222PR/zibal-payment?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/Mohammad222PR/zibal-payment?style=flat-square)
![GitHub Issues](https://img.shields.io/github/issues/Mohammad222PR/zibal-payment?style=flat-square)
![GitHub License](https://img.shields.io/github/license/Mohammad222PR/zibal-payment?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)

A simple Python library to integrate with the **Zibal Payment Gateway**. This package provides methods to request payments, verify them, and generate payment URLs for use in your web or mobile applications.

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Initialize Zibal Class](#1-initialize-zibal-class)
  - [2. Request Payment](#2-request-payment)
  - [3. Generate Payment URL](#3-generate-payment-url)
  - [4. Verify Payment](#4-verify-payment)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Support](#support)
- [License](#license)

---

## **Features**
- Easy integration with Zibal payment gateway.
- Handles payment request, URL generation, and payment verification.
- Supports custom callback URLs.
- Clean and simple API for developers.

---

## **Installation**

1. Clone the repository:
    ```bash
    git clone https://github.com/Mohammad222PR/zibal-payment.git
    ```
2. Install dependencies (if any):
    ```bash
    pip install requests
    ```

---

## **Usage**

### **1. Initialize Zibal Class**

Initialize the `Zibal` class with your **Merchant ID** from Zibal. You can pass the Merchant ID directly or set it as an environment variable (`ZIBAL_PAYMENT_MERCHANT_ID`).

```python
from zibal import Zibal

# Initialize Zibal with merchant ID
zibal = Zibal(merchant_id="your_merchant_id")
```

### **2. Request Payment**

To request a payment, use the `payment_request` method by passing the amount in **Rials** and an optional description.

```python
response = zibal.payment_request(amount=150000, description="پرداخت برای خرید محصول")
print(response)

# Sample Response
# {'result': 100, 'trackId': '123456', 'message': 'Success'}
```

### **3. Generate Payment URL**

Once you have the `trackId` from the payment request, you can generate the payment URL to redirect the user.

```python
payment_url = zibal.generate_payment_url(track_id=response["trackId"])
print(payment_url)

# Sample URL
# https://gateway.zibal.ir/start/123456
```

### **4. Verify Payment**

After the payment process, use the `payment_verify` method with the `trackId` to verify if the payment was successful.

```python
verification_response = zibal.payment_verify(track_id=response["trackId"])
print(verification_response)

# Sample Response
# {'result': 100, 'paidAt': '2024-10-10T12:00:00Z', 'status': 1, 'message': 'Payment verified successfully'}
```

---

## **Environment Variables**

You can store your **Merchant ID** in the environment variable `ZIBAL_PAYMENT_MERCHANT_ID` to avoid hardcoding it into your code.

Example:
```bash
export ZIBAL_PAYMENT_MERCHANT_ID="your_merchant_id"
```

The `Zibal` class will automatically pick up the merchant ID from this variable unless explicitly passed in the constructor.

---

## **Testing**

For testing purposes, you can use tools like `smtp4dev` for email notifications or Zibal's sandbox environment. Make sure to replace the callback URL with your test environment.

---

## **Support**

If you encounter any issues, feel free to open an issue on [GitHub](https://github.com/Mohammad222PR/zibal-payment/issues). You can also check out the official documentation for Zibal's API [here](https://docs.zibal.ir).

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> **Designed & Developed by Mohammad Hossein** ✨

![Zibal Payment](https://github.com/user-attachments/assets/bd12dfd0-6670-4d6f-b3d5-b1d7a4ff579a)


---
