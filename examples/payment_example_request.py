
from zibal_payment.client import ZibalClient
from zibal_payment.exceptions import ZibalError

def example_payment_request():
    merchant_id = "test_merchant"
    client = ZibalClient(merchant_id)

    try:
        response = client.payment_request(amount=1000, callback_url="https://example.com", description="Test payment")
        track_id = response.get('trackId')
        payment_url = client.generate_payment_url(track_id)
        print(f"Payment URL: {payment_url}")
    except ZibalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    example_payment_request()
