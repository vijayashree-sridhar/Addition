from calculate import calculate

def test_calculate_sum():
    assert calculate(2, 3, 1) == 5
    assert calculate(2, 2, 1) == 4
    assert calculate(20, 1, 1) == 21
    assert calculate(2, 10, 1) == 12
    assert calculate(2, 3, 2) == -1
    assert calculate(2, 2, 2) == 0
    assert calculate(20, 1, 2) == 19
    assert calculate(2, 10, 2) == -8
    assert calculate(2, 3, 3) == 6
    assert calculate(2, 2, 3) == 4
    assert calculate(20, 1, 3) == 20
    assert calculate(2, 10, 3) == 20
    assert calculate(6, 3, 4) == 2
    assert calculate(2, 2, 4) == 1
    assert calculate(20, 1, 4) == 20
    assert calculate(10, 2, 4) == 5
    assert calculate(3, 2, 5) == 1
    assert calculate(2, 2, 5) == 0
    assert calculate(20, 1, 5) == 0
    assert calculate(8, 3, 5) == 2
    assert calculate(3, 2, 6) == 9
    assert calculate(2, 2, 6) == 4
    assert calculate(20, 1, 6) == 20
    assert calculate(8, 3, 6) == 512
