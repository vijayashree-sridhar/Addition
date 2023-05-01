from calculate_sum import calculate_sum
import sys

def test_calculate_sum():
    assert calculate_sum(sys.argv[0], sys.argv[1]) == sys.argv[2]
