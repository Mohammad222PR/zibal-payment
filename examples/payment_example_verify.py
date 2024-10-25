from zibal_payment.client import ZibalClient
from zibal_payment.exceptions import ZibalError

def example_payment_verify(track_id: str):
    merchant_id = "test_merchant"
    client = ZibalClient(merchant_id)

    try:
        # تأیید پرداخت
        response = client.payment_verify(track_id)
        print(f"Verification response: {response}")
    except ZibalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    example_payment_verify("1234567890")
