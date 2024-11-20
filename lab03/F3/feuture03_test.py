from feature03 import less, sort_score, higher

def test_less():
    assert less([1, 2, 3, 4, 5], 3) == [1, 2]
    assert less([10, 20, 30, 40], 25) == [10, 20]
    assert less([5, 15, 25, 35], 40) == [5, 15, 25, 35]
    assert less([5, 15, 25, 35], 5) == []

def test_sort_score():
    assert sort_score([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]
    assert sort_score([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
    assert sort_score([5, 5, 5]) == [5, 5, 5]
    assert sort_score([1]) == [1]

def test_highter():
    assert higher([1, 2, 3, 4, 5], 3) == [4, 5]
    assert higher([10, 20, 30, 40], 25) == [30, 40]
    assert higher([5, 15, 25, 35], 5) == [15, 25, 35]
    assert higher([5, 15, 25, 35], 35) == []

if __name__ == '__main__':
    test_less()
    test_sort_score()
    test_highter()
