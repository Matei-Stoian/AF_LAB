
def less(score_list:list[int],value:int) -> list[int]:
    """
    Computers a list where any score is less than the value.

    Parameters:
        score_list  (list[int]): The list of scores.
        value   (int):  The value to compare with.
    
    Returns:
        (list[int]): A list whre every element is less then the value.
    """
    return [x for x in score_list if x < value]

def sort_score(score_list:list[int]) -> list[int]:
    """
    Sorts the list.

    Parameters:
        score_list  (list[int]):The score list.
    
    Return:
        (list[int]): The sorted list.
    """
    score_list_copy = score_list.copy()
    new_list = [(x,y) for x,y in enumerate(score_list)]
    new_list.sort(key= lambda x: x[1])
    return [x[0] for x in new_list]


def higher(score_list:list[int],value) -> list[int]:
    """
    Computers a list where any score is higher than the value.

    Parameters:
        score_list  (list[int]): The list of scores.
        value   (int):  The value to compare with.
    
    Returns:
        (list[int]): A list whre every element is higher then the value.
    """
    return [x for x in sorted(score_list) if x > value]
        

if __name__ == '__main__':
    sort_score([1,4,3,5,6])