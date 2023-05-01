from calculate_sum import calculate_sum

def pytest_addoption(parser):
    parser.addoption("--a", action="store", type=int, help="first number")
    parser.addoption("--b", action="store", type=int, help="second number")

def test_calculate_sum(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    result = calculate_sum(a, b)
    assert result == a + b


# def test_calculate_sum():
#     assert calculate_sum(2, 3) == 5
