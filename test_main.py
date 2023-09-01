"""
Test goes here

"""
from main import negative_number


def test_negative_number():
    # Test with a positive number
    result = negative_number(-1)
    assert result, "Test failed for the negative number"


if __name__ == "__main__":
    test_negative_number()