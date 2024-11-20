from feature01 import add,insert 

def test_add():

    assert add([1,2,3,4,5],6) == [1,2,3,4,5,6]
    assert add([],4) == [4]
    assert add([100,3,4],0) == [100,3,4,0]

def test_insert():

    assert insert([1,2,4],0,3) == [3,1,2,4]
    assert insert([1,3,4],2,6) == [1,3,6,4]
    assert insert([1,2,2],3,3) == [1,2,2,3]


if __name__ == '__main__':
    test_add()
    test_insert()