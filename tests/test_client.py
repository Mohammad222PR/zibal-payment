import pytest
import requests

from unittest.mock import patch, Mock

from zibal_payment.client import ZibalClient
from zibal_payment.exceptions import ZibalError


@pytest.fixture
def zibal_client():
    return ZibalClient(merchant_id="test_merchant", sandbox=True)


# ----- Payment Request Tests -----

@patch('zibal_payment.client.requests.post')
def test_payment_request_success(mock_post, zibal_client):
    # Mock a successful response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 100, 'trackId': '12345'}
    mock_post.return_value = mock_response

    response = zibal_client.payment_request(amount=1000, callback_url="https://example.com", description="Test payment")

    assert response['result'] == 100
    assert response['trackId'] == '12345'


@patch('zibal_payment.client.requests.post')
def test_payment_request_failure(mock_post, zibal_client):
    # Mock a failed response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 101, 'message': 'Payment failed'}
    mock_post.return_value = mock_response

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_request(amount=1000, callback_url="https://example.com", description="Test payment")

    assert "Payment request failed" in str(excinfo.value)


@patch('zibal_payment.client.requests.post')
def test_payment_request_invalid_amount(mock_post, zibal_client):
    # Mock an invalid amount response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 102, 'message': 'Invalid amount'}
    mock_post.return_value = mock_response

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_request(amount=0, callback_url="https://example.com", description="Invalid payment")

    assert "Payment request failed" in str(excinfo.value)


@patch('zibal_payment.client.requests.post')
def test_payment_request_network_error(mock_post, zibal_client):
    # Mock a network error (e.g., timeout)
    mock_post.side_effect = requests.RequestException("Network error")

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_request(amount=1000, callback_url="https://example.com", description="Test payment")

    assert "Network error occurred during the payment request" in str(excinfo.value)


# ----- Payment Verify Tests -----

@patch('zibal_payment.client.requests.post')
def test_payment_verify_success(mock_post, zibal_client):
    # Mock a successful verification response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 100, 'paidAt': '2024-10-01'}
    mock_post.return_value = mock_response

    response = zibal_client.payment_verify(track_id='12345')

    assert response['result'] == 100
    assert response['paidAt'] == '2024-10-01'


@patch('zibal_payment.client.requests.post')
def test_payment_verify_failure(mock_post, zibal_client):
    # Mock a failed verification response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 101, 'message': 'Verification failed'}
    mock_post.return_value = mock_response

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_verify(track_id='12345')

    assert "An error occurred during the payment verification" in str(excinfo.value)


@patch('zibal_payment.client.requests.post')
def test_payment_verify_invalid_track_id(mock_post, zibal_client):
    # Mock an invalid track ID response
    mock_response = Mock()
    mock_response.json.return_value = {'result': 102, 'message': 'Invalid track ID'}
    mock_post.return_value = mock_response

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_verify(track_id='invalid_track_id')

    assert "An error occurred during the payment verification" in str(excinfo.value)



# ----- Timeout and Performance Tests -----

@patch('zibal_payment.client.requests.post')
def test_payment_request_timeout(mock_post, zibal_client):
    # Mock a timeout response
    mock_post.side_effect = requests.Timeout("Request timed out")

    with pytest.raises(ZibalError) as excinfo:
        zibal_client.payment_request(amount=1000, callback_url="https://example.com", description="Test payment")

    assert "Request timed out" in str(excinfo.value)