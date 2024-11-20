from feature05 import filter_mul, filter_greater

def test_filter_mul():
    assert filter_mul([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    assert filter_mul([10, 15, 20, 25, 30], 5) == [10, 15, 20, 25, 30]
    assert filter_mul([1, 3, 5, 7], 2) == []
    assert filter_mul([8, 12, 16, 20], 4) == [8, 12, 16, 20]
    assert filter_mul([], 3) == []

def test_filter_greater():
    assert filter_greater([1, 2, 3, 4, 5], 3) == [4, 5]
    assert filter_greater([10, 20, 30, 40], 25) == [30, 40]
    assert filter_greater([5, 15, 25, 35], 5) == [15, 25, 35]
    assert filter_greater([5, 15, 25, 35], 35) == []
    assert filter_greater([], 10) == []

if __name__ == '__main__':
    test_filter_mul()
    test_filter_greater()
