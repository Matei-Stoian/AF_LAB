def avg(score_list: list[int], from_index: int, to_index: int) -> int:
    """
    Compute the avrage score between two indices.

    Parameters:
        score_list  (list[int]): The list of scores.
        from_index  (int): The first index.
        to_index    (int):  The second index.

    Return:
        (int): The average score.
    """
    return sum(score_list[from_index:to_index+1])//(to_index-from_index+1) if score_list[from_index:to_index+1] else 0 


def find_min(score_list: list[int], from_index: int, to_index: int) -> int:
    """
    Compute the minimum score between two indices.

    Parameters:
        score_list  (list[int]): The list of scores.
        from_index  (int): The first index.
        to_index    (int):  The second index.

    Return:
        (int): The minimum score.

    """
    return min(score_list[from_index:to_index + 1])

def mul(score_list: list[int], value: int, from_index: int, to_index: int) -> list[int]:
    """
    Compute a list where every element is equal to the score from the score list time the value.

    Parameters:
        score_list  (list[int]): The list of scores.
        value   (int): The value to multiply with.
        from_index  (int): The first index.
        to_index    (int):  The second index.

    Return:
        (list[int]): The list of the values mutilplied.

    """
    to_index = min(to_index,len(score_list)-1)

    return [score_list[i] * value for i in range(from_index, to_index + 1)]
