from calculate import calculate

def test_calculate_sum():
    assert calculate_sum(2, 3, 1) == 5
    assert calculate_sum(2, 2, 1) == 4
    assert calculate_sum(20, 1, 1) == 21
    assert calculate_sum(2, 10, 1) == 12
