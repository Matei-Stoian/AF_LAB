def filter_mul(score_list:list[int],value:int) -> list[int]:
    """
    Filters all the scores that are not mutipels of value.

    Parameters:
        score_list (list[int]): The list of scores.
        value (int): The value to check for.
    
    Return:
        (list[int]): The filtered list.
    """
    return [x for x in score_list if x%value == 0]

def filter_greater(score_list:list[int],value:int) -> list[int]:
    """
    Filters all the scores that are less or equal to the value.

    Parameters:
        score_list  (list[int]): The list of scors.
        value   (int): The value to check for.
    
    Return:
        (list[int]): All the scores greater than the value.
    """
    return [x for x in score_list if x > value]
