from calculate import calculate

def test_calculate_sum():
    assert calculate(2, 3, 1) == 5
    assert calculate(2, 2, 1) == 4
    assert calculate(20, 1, 1) == 21
    assert calculate(2, 10, 1) == 12
