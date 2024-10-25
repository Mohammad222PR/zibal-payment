from zibal_payment.client import ZibalDjango
from django.shortcuts import redirect

def make_payment(request):
    """
    Example view to create a payment request using ZibalDjango.
    """
    # Create an instance of ZibalDjango that gets values from settings.py
    zibal_client = ZibalDjango()

    try:
        # Send a payment request to Zibal using payment_request
        payment_data = zibal_client.payment_request(
            amount=50000,  # Payment amount in Rials (e.g., 50,000 Rials)
            callback_url="https://your-site.com/callback",  # Callback URL after payment
            description="Test Product Purchase"  # Payment description
        )

        # Redirect user to the Zibal payment page
        return redirect(payment_data['url'])

    except Exception as e:
        # Handle errors (such as network issues with Zibal)
        print(f"Error creating payment request: {e}")
        return redirect("https://your-site.com/error")


def payment_callback(request):
    """
    Example view to handle the payment callback and verify the payment.
    """
    # Get the trackId from the URL that Zibal sends after payment
    track_id = request.GET.get('trackId')

    if not track_id:
        return redirect("https://your-site.com/error")

    zibal_client = ZibalDjango()

    try:
        # Verify the payment using trackId
        verification_data = zibal_client.payment_verify(track_id)

        if verification_data['result'] == 100:
            # Payment was successful
            print("Payment was successful.")
            return redirect("https://your-site.com/success")

        else:
            # Payment verification failed
            print(f"Error verifying payment: {verification_data['message']}")
            return redirect("https://your-site.com/failure")

    except Exception as e:
        # Handle errors during payment verification
        print(f"Error verifying payment: {e}")
        return redirect("https://your-site.com/error")
