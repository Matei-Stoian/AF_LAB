
def remove(score_list:list[int],from_index:int,to_index:int=None) ->list[int]:
    """
        Removes the elements from a specific index or from a to remove from two indices.

        Parmeters:
            score_list (list[int]): The list of scores.
            from_index (int): The first index.
            to_index (int): The second index. Default = None.
        Return:
            (list[int]): The modified list. 
    """
    if to_index is None:
        score_list.pop(from_index)
    else:
        remove_list = score_list[from_index:to_index+1]
        for i in remove_list:
            score_list.remove(i)
    return score_list
        


def replace(score_list:list[int],index:int,new_value:int) -> list[int]:
    """
    Replace a the value from a index in the score list with the new given value.

    Parameters:
        Parmeters:
            score_list (list[int]): The list of scores.
            index (int): The index to modify.
            value (int): The value to replace with.
        Return:
            (list[int]): The modified list. 
    """
    score_list[index] = new_value

    return score_list





