from myvector import MyVector
import matplotlib.pyplot as plt
import random


class VectorRepository:
    """
    A repository for managing a collection of MyVector objects.
    """

    def __init__(self):
        """
        Initializes an empty list to store vectors.
        """
        self.__vectors: list[MyVector] = []

    def add_vector(self, vector: MyVector):
        """
        Adds a new vector to the repository.

        Args:
            vector (MyVector): The vector to add.
        """
        self.__vectors.append(vector)

    def get_all_vectors(self) -> list[MyVector]:
        """
        Returns all vectors in the repository.

        Returns:
            list[MyVector]: The list of vectors.
        """
        return self.__vectors

    def get_vector_by_index(self, index: int) -> MyVector:
        """
        Retrieves a vector by its index.

        Args:
            index (int): The index of the vector to retrieve.

        Returns:
            MyVector: The vector at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.__vectors):
            raise IndexError("Index out of range.")
        return self.__vectors[index]

    def update_vector_by_index(self, index: int, name_id=None, color=None, vector_type=None, values=None):
        """
        Updates a vector at a given index with new attributes.

        Args:
            index (int): The index of the vector to update.
            name_id (str | int | None): The new name ID, or None to leave unchanged.
            color (str | None): The new color, or None to leave unchanged.
            vector_type (int | None): The new type, or None to leave unchanged.
            values (list[int] | None): The new values, or None to leave unchanged.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.__vectors):
            raise IndexError("Index out of range.")

        vector = self.__vectors[index]
        if name_id is not None:
            vector.set_name_id(name_id)
        if color is not None:
            vector.set_color(color)
        if vector_type is not None:
            vector.set_type(vector_type)
        if values is not None:
            vector.set_values(values)

    def update_vector_by_name_id(self, check_name_id, **kwargs):
        """
        Updates a vector by its name ID with new attributes.

        Args:
            name_id (str | int): The name ID of the vector to update.
            kwargs: Attributes to update (e.g., name_id, color, type, values).

        Raises:
            ValueError: If no vector with the specified name ID is found.
        """
        for vector in self.__vectors:
            if vector.get_name_id() == check_name_id:
                self.update_vector_by_index(self.__vectors.index(vector), **kwargs)
                return
        raise ValueError(f"No vector found with name_id {check_name_id}.")

    def delete_vector_by_index(self, index: int):
        """
        Deletes a vector by its index.

        Args:
            index (int): The index of the vector to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.__vectors):
            raise IndexError("Index out of range.")
        self.__vectors.pop(index)

    def delete_vector_by_name_id(self, name_id: str | int):
        """
        Deletes a vector by its name ID.

        Args:
            name_id (str | int): The name ID of the vector to delete.

        Raises:
            ValueError: If no vector with the specified name ID is found.
        """
        poz = 0
        for i,vector in enumerate(self.__vectors):
            if vector.get_name_id() == name_id:
                poz = i
                break
        self.delete_vector_by_index(poz)

    def plot__vectors(self):
        """
        Plots the vectors in a 3D space using Matplotlib.

        Different shapes represent different types of vectors.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        shapes = {1: "o", 2: "s", 3: "^"}
        for vector in self.__vectors:
            x, y, z = vector.get_values()
            marker = shapes.get(vector.get_type(), "D")  
            ax.scatter(x, y, z, c=vector.get_color(), marker=marker)

        plt.show()

    def get_sum_of_all__vectors(self) -> int:
        """
        Calculates the sum of all vector values in the repository.

        Returns:
            int: The total sum of all vector values.
        """
        return sum(vector.get_sum() for vector in self.__vectors)

    def delete_all__vectors(self):
        """
        Deletes all vectors from the repository.
        """
        self.__vectors.clear()

    def set_color_for_type(self, vector_type: int, color: str):
        """
        Sets the color for all vectors of a given type.

        Args:
            vector_type (int): The type of vectors to update.
            color (str): The new color.

        Raises:
            ValueError: If the color is invalid or the type is less than 1.
        """
        if color not in ["r", "y", "g", "b", "m"]:
            raise ValueError("Invalid color.")
        if not isinstance(vector_type, int) or vector_type < 1:
            raise ValueError("Type must be an integer greater than or equal to 1.")

        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_type() == vector_type:
                self.__vectors[i].set_color(color=color)


if __name__ == "__main__":
    colors = ["r", "y", "g", "b", "m"]
    repo = VectorRepository()

    # Add 10 random vectors
    for _ in range(10):
        name_id = random.choice([random.randint(1, 100), f"name_{random.randint(1, 100)}"])
        color = random.choice(colors)
        vector_type = random.randint(1, 8)
        values = [random.randint(-50, 50) for _ in range(3)]

        vector = MyVector(name_id=name_id, color=color, type=vector_type, values=values)
        repo.add_vector(vector)

    repo.plot__vectors()
