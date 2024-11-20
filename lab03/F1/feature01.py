def add(score_list: list[int], value: int) -> list[int]:
    """
    Append a given value to the score list.

    Parameters:
        score_list (list[int]): the score list.
        value (int): the value to be added.
    Return:
            (list[int]): The modified list.
    """
    score_list.append(value)
    return score_list


def insert(score_list: list[int], index: int, value: int) -> list[int]:
    """
    Insert a value to a specific index in the score list.

    Parameters:
        score_list (list[int]): The score list.
        index (int): The index to add the value.
        value (int): The value to be added.
    Return:
            (list[int]): The modified list.
    """
    score_list.insert(index, value)
    return score_list
