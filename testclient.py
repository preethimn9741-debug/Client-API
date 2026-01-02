import pytest
from unittest.mock import patch
import client


class Args:
    def __init__(self, command, to=None, amount=None):
        self.command = command
        self.to = to
        self.amount = amount



def test_valid_convert_args():
    args = Args("convert", "INR", 10)
    assert client.validate_args(args) is True


def test_missing_arguments():
    args = Args("convert", None, None)
    with pytest.raises(ValueError):
        client.validate_args(args)


def test_negative_amount():
    args = Args("convert", "INR", -5)
    with pytest.raises(ValueError):
        client.validate_args(args)



@patch("client.requests.get")
def test_fetch_rates_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "rates": {"INR": 83.0}
    }

    data = client.fetch_rates("USD")
    assert "rates" in data
    assert data["rates"]["INR"] == 83.0


@patch("client.requests.get")
def test_fetch_rates_failure(mock_get):
    mock_get.side_effect = Exception("Network error")

    with pytest.raises(Exception):
        client.fetch_rates("USD")
