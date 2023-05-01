from calculate_sum import calculate_sum

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(2, 2) == 4
    assert calculate_sum(2, 1) == 4
    assert calculate_sum(2, 1) == 2
