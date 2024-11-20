from feature04 import avg, find_min, mul

def test_avg():
    assert avg([1, 2, 3, 4, 5], 0, 2) == 2  
    assert avg([10, 20, 30, 40, 50], 1, 3) == 30  
    assert avg([5, 5, 5, 5], 0, 3) == 5
    assert avg([10, 15, 20], 0, 1) == 12  
def test_find_min():
    assert find_min([1, 2, 3, 4, 5], 0, 2) == 1
    assert find_min([10, 20, 5, 40, 50], 1, 3) == 5
    assert find_min([5, 15, 25, 35], 0, 3) == 5
    assert find_min([7, 3, 8, 2, 9], 2, 4) == 2
 

def test_mul():
    assert mul([1, 2, 3, 4, 5], 2, 0, 2) == [2, 4, 6]  
    assert mul([10, 20, 30, 40], 3, 1, 3) == [60, 90, 120]  
    assert mul([5, 10, 15, 20], 0, 0, 3) == [0, 0, 0, 0]  
    assert mul([5, 15, 25], -1, 1, 2) == [-15, -25]  

if __name__ == '__main__':
    test_avg()
    test_find_min()
    test_mul()
