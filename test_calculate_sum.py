# from calculate_sum import calculate_sum

# def pytest_addoption(parser):
#     parser.addoption("--a", action="store", type=int, help="first number")
#     parser.addoption("--b", action="store", type=int, help="second number")

# def test_calculate_sum(request):
#     a = request.config.getoption("--a")
#     b = request.config.getoption("--b")
#     result = calculate_sum(a, b)
#     assert result == a + b


# def test_calculate_sum():
#     assert calculate_sum(2, 3) == 5

import pytest
import argparse

def calculate_sum(a, b):
    return a + b

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5

@pytest.mark.parametrize("a, b, expected_sum", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 2, 1),
])
def test_calculate_sum_parametrized(a, b, expected_sum):
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=int, default=a)
    parser.add_argument("-b", type=int, default=b)
    args = parser.parse_args()
    assert calculate_sum(args.a, args.b) == expected_sum

