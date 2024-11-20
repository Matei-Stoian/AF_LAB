from feature02 import remove,replace


def test_remove1():
    assert remove([1,2,3,4,5],0) == [2,3,4,5]
    assert remove([1,2,3,4,5],1) == [1,3,4,5]
    assert remove([1,2,3,4,5],2) == [1,2,4,5]

def test_remove2():
    assert remove([1,2,3,4,5],0,2) == [4,5]
    assert remove([1,2,3,4,5],1,2) == [1,4,5]
    assert remove([1,2,3,4,5],2,4) == [1,2]

def test_replace():
    assert replace([1,2,3,4,5],0,9) == [9,2,3,4,5]
    assert replace([1,2,3,4,5],1,9) == [1,9,3,4,5]
    assert replace([1,2,3,4,5],4,9) == [1,2,3,4,9]


if __name__ == '__main__':
    test_remove1()
    test_remove2()
    test_replace()