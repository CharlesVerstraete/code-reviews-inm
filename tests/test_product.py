from inm_package.product import product


def test_product():
    # Test with positive numbers
    assert product(2, 3) == 6
    # Test with zero
    assert product(0, 3) == 0
    assert product(3, 0) == 0
    # Test with a negative number
    assert product(-1, 10) == -10
    # Test with two negative numbers
    assert product(-2, -3) == 6
    # Test with floats
    assert product(2.5, 4) == 10.0
