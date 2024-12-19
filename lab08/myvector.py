import numpy as np

class MyVector:
    """
    A class to represent a mathematical vector with additional metadata.

    Attributes:
        name_id (str | int): The identifier of the vector (either a string or an integer).
        color (str): The color of the vector, must be one of ["r", "y", "g", "b", "m"].
        type (int): The type of the vector, must be an integer >= 1.
        values (np.ndarray): The numerical values of the vector as a NumPy array.
    """

    def __init__(self, name_id: str | int, color: str, type: int, values: list[int] | np.ndarray):
        """
        Initializes a new vector instance with the given attributes.

        Args:
            name_id (str | int): The identifier for the vector.
            color (str): The color of the vector, must be one of ["r", "y", "g", "b", "m"].
            type (int): The type of the vector, must be an integer >= 1.
            values (list[int] | np.ndarray): The numerical values of the vector.

        Raises:
            ValueError: If any attribute is invalid.
        """
        if not isinstance(name_id, (str, int)):
            raise ValueError("The name_id must be a string or an integer.")
        if color not in ["r", "y", "g", "b", "m"]:
            raise ValueError("Invalid color. Must be one of ['r', 'y', 'g', 'b', 'm'].")
        if not isinstance(type, int) or type < 1:
            raise ValueError("Type must be an integer >= 1.")
        if not all(isinstance(value, int) for value in values):
            raise ValueError("All values must be integers.")

        self.__name_id = name_id
        self.__color = color
        self.__type = type
        self.__values = np.array(values, dtype=np.integer)

    def get_name_id(self) -> str | int:
        """Returns the vector's identifier."""
        return self.__name_id

    def get_color(self) -> str:
        """Returns the vector's color."""
        return self.__color

    def get_type(self) -> int:
        """Returns the vector's type."""
        return self.__type

    def get_values(self) -> list[int]:
        """Returns the vector's values as a list."""
        return self.__values.tolist()

    def get_numpy_values(self) -> np.ndarray:
        """Returns the vector's values as a NumPy array."""
        return self.__values

    def set_name_id(self, new_name_id: str | int):
        """
        Updates the vector's identifier.

        Args:
            new_name_id (str | int): The new identifier for the vector.

        Raises:
            ValueError: If the new identifier is not a string or integer.
        """
        if not isinstance(new_name_id, (str, int)):
            raise ValueError("The name_id must be a string or an integer.")
        self.__name_id = new_name_id

    def set_color(self, color: str):
        """
        Updates the vector's color.

        Args:
            color (str): The new color, must be one of ["r", "y", "g", "b", "m"].

        Raises:
            ValueError: If the color is invalid.
        """
        if color not in ["r", "y", "g", "b", "m"]:
            raise ValueError("Invalid color. Must be one of ['r', 'y', 'g', 'b', 'm'].")
        self.__color = color

    def set_type(self, type: int):
        """
        Updates the vector's type.

        Args:
            type (int): The new type, must be an integer >= 1.

        Raises:
            ValueError: If the type is invalid.
        """
        if not isinstance(type, int) or type < 1:
            raise ValueError("Type must be an integer >= 1.")
        self.__type = type

    def set_values(self, values: list[int] | np.ndarray):
        """
        Updates the vector's values.

        Args:
            values (list[int] | np.ndarray): The new values for the vector.

        Raises:
            ValueError: If any value is not an integer.
        """
        if not all(isinstance(value, int) for value in values):
            raise ValueError("All values must be integers.")
        self.__values = np.array(values, dtype=np.integer)

    def add_scalar(self, scalar: int):
        """
        Adds a scalar value to each element of the vector.

        Args:
            scalar (int): The scalar value to add.
        """
        self.__values += scalar

    def __add__(self, other: "MyVector"):
        """
        Adds another vector to this vector.

        Args:
            other (MyVector): The vector to add.

        Raises:
            ValueError: If the vectors have different sizes.
        """
        if len(other.get_values()) != len(self.__values):
            raise ValueError("Vectors must have the same size.")
        self.__values += other.get_numpy_values()

    def __sub__(self, other: "MyVector"):
        """
        Subtracts another vector from this vector.

        Args:
            other (MyVector): The vector to subtract.

        Raises:
            ValueError: If the vectors have different sizes.
        """
        if len(other.get_values()) != len(self.__values):
            raise ValueError("Vectors must have the same size.")
        self.__values -= other.get_numpy_values()

    def __mul__(self, other: "MyVector") -> int:
        """
        Computes the dot product of this vector and another vector.

        Args:
            other (MyVector): The other vector.

        Returns:
            int: The dot product result.

        Raises:
            ValueError: If the vectors have different sizes.
        """
        if len(other.get_values()) != len(self.__values):
            raise ValueError("Vectors must have the same size.")
        return int(np.dot(self.__values, other.get_numpy_values()))

    def get_sum(self) -> int:
        """Returns the sum of the vector's elements."""
        return int(np.sum(self.__values))

    def get_product(self) -> int:
        """Returns the product of the vector's elements."""
        return int(np.prod(self.__values))

    def get_avg(self) -> int:
        """Returns the average of the vector's elements."""
        return self.get_sum() // len(self.__values)

    def get_min(self) -> int:
        """Returns the smallest value in the vector."""
        return int(np.min(self.__values))

    def get_max(self) -> int:
        """Returns the largest value in the vector."""
        return int(np.max(self.__values))

    def __str__(self) -> str:
        """Returns a string representation of the vector."""
        return f"Vector(name_id={self.__name_id}, color={self.__color}, type={self.__type}, values={self.__values.tolist()})"

    def __repr__(self) -> str:
        """Returns a detailed string representation of the vector."""
        return f"MyVector(name_id={self.__name_id}, color={self.__color}, type={self.__type}, values={self.__values.tolist()})"


if __name__ == "__main__":
    vec1 = MyVector(1, "r", 1, [1, 2, 3])
    vec2 = MyVector(2, "g", 1, [4, 5, 6])
    print(vec1)
    print(vec2)
    vec1.add_scalar(2)
    print(vec1)
    vec1 + vec2
    print(vec1)
