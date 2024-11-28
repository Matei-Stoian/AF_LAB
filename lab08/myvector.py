import numpy as np


class MyVector:

    def __init__(self, name_id: str | int, color: str, type: int, values: list[int]):

        if not isinstance(name_id, (str, int)):
            raise ValueError("The name_id must be a int or a string.")
        else:
            self.__name_id = name_id

        if color not in ["r", "y", "g", "b", "m"]:
            raise ValueError("Not a valid color.")
        else:
            self.__color = color

        if isinstance(type, int) == True and type >= 1:
            self.__type = type
        else:
            raise ValueError("Type must be a int greater or equal to 1.")

        for value in values:
            if isinstance(value, int) == False:
                raise ValueError("All the values must be of type int.")

        self.__values = np.array(values)

    def get_name_id(self) -> str | int:
        return self.__name_id

    def get_color(self) -> str:
        return self.__color

    def get_type(self) -> int:
        return self.__type

    def get_values(self) -> list[int]:
        return self.__values

    def set_name_id(self, new_name_id: str | int):
        if not isinstance(new_name_id, (str, int)):
            raise ValueError("The name_id must be a int or a string.")
        else:
            self.__name_id = new_name_id

    def set_color(self, color: str):
        if color not in ["r", "y", "g", "b", "m"]:
            raise ValueError("Not a valid color.")
        else:
            self.__color = color

    def set_type(self, type: int):
        if isinstance(type, int) == True and type >= 1:
            self.__type = type
        else:
            raise ValueError("Type must be a int greater or equal to 1.")

    def set_values(self, values: list[int]):
        for value in values:
            if isinstance(value, int) == False:
                raise ValueError("All the values must be of type int.")

        self.__values = values

    def add_scalar(self, scalar):
        self.__values = [scalar + value for value in self.__values]

    def __add__(self, other: "MyVector"):
        if len(other.get_values()) != len(self.__values):
            raise ValueError("The vectors must have the same size.")

        result_vector = self.__values + other.get_values()

        self.__values = result_vector

    def __sub__(self, other: "MyVector"):
        if len(other.get_values()) != len(self.__values):
            raise ValueError("The vectors must have the same size.")
        result_vector = self.__values - other.get_values()

        self.__values = result_vector

    def __mul__(self, other: "MyVector") -> int:
        if len(other.get_values()) != len(self.__values):
            raise ValueError("The vectors must have the same size.")

        ans = 0
        for i, j in zip(self.__values, other.get_values()):
            ans += i * j

        return ans

    def get_sum(self) -> int:
        return sum(self.__values)

    def get_product(self) -> int:
        prod = 1
        for i in self.__values:
            prod *= i

        return prod

    def get_avg(self) -> int:
        n = len(self.__values)

        return self.get_sum() // n

    def get_min(self) -> int:
        return min(self.__values)

    def get_max(self) -> int:
        return max(self.__values)

    def __str__(self) -> str:
        return f"Vector name_id:{self.__name_id},color:{self.__color},type:{self.__type},values:{self.__values}"

    def __repr__(self) -> str:
        return f"MyVector(name_id:{self.__name_id},color:{self.__color},type:{self.__type},values:{self.__values})"


if __name__ == "__main__":

    vec1 = MyVector(1, "r", 1, [1, 2, 3])
    vec2 = MyVector(2, "g", 1, [2, 3, 4])
    print(vec1)
    print(vec2)
    vec1.add_scalar(2)
    print(vec1)
    vec1 + vec2
    print(vec1)
