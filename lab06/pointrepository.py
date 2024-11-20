from mypoint import MyPoint
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")


class PointRepository:
    """
    A repository for managing points with coordinates and colors.
    """

    def __init__(self):
        """
        Initialize the repository with an empty list of points.

        Parameters:
            None

        Return:
            None
        """
        self.__points: list[MyPoint] = []

    def addPoint(self, point: MyPoint):
        """
        Add a new point to the repository.

        Parameters:
            point (MyPoint): The point to be added.

        Return:
            None
        """
        self.__points.append(point)

    def getAllPoints(self) -> list[MyPoint]:
        """
        Retrieve all points in the repository.

        Parameters:
            None

        Return:
            (list[MyPoint]): A list of all points.
        """
        return self.__points

    def getAllPointsColor(self, color: str) -> list[MyPoint]:
        """
        Retrieve all points with a specified color.

        Parameters:
            color (str): The color to filter points (e.g., "red", "blue").

        Return:
            (list[MyPoint]): A list of points with the specified color.
        """
        if color not in ["red", "green", "blue", "yellow", "magenta"]:
            return []
        return [point for point in self.__points if point.get_color() == color]

    @staticmethod
    def __distance(point1: MyPoint, point2: MyPoint) -> float:
        """
        Calculate the Euclidean distance between two points.

        Parameters:
            point1 (MyPoint): The first point.
            point2 (MyPoint): The second point.

        Return:
            (float): The distance between the two points.
        """
        x1, y1 = point1.get_point()
        x2, y2 = point2.get_point()
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def minDistance(self) -> float:
        """
        Calculate the minimum distance between any two points in the repository.

        Parameters:
            None

        Return:
            (float): The minimum distance, or infinity if fewer than two points exist.
        """
        if len(self.__points) < 2:
            return float("inf")

        ans = float("inf")
        for i, point1 in enumerate(self.__points):
            for point2 in self.__points[i + 1 :]:
                ans = min(ans, self.__distance(point1, point2))
        return ans

    def getPointsInSquare(self, corner: tuple[float,float], length: int) -> list[MyPoint]:
        """
        Retrieve all points within a square defined by the top-left corner and side length.

        Parameters:
            corner (MyPoint): The top-left corner of the square.
            length (int): The length of the square's side.

        Return:
            (list[MyPoint]): A list of points inside the square.
        """
        x_min, y_max = corner
        x_max = x_min + length
        y_min = y_max - length
        return [
            point
            for point in self.__points
            if x_min <= point.get_x() <= x_max and y_min <= point.get_y() <= y_max
        ]

    def removePointsFromSquare(self, corner: tuple[float,float], length: int) -> int:
        """
        Remove all points within a square defined by the top-left corner and side length.

        Parameters:
            corner (MyPoint): The top-left corner of the square.
            length (int): The length of the square's side.

        Return:
            (int): Number of ponints deleted
        """
        x_min, y_max = corner

        x_max = x_min + length
        y_min = y_max - length

        n = len(self.__points)
        self.__points = [
            point
            for point in self.__points
            if not (x_min <= point.get_x() < x_max and y_min <= point.get_y() < y_max)
        ]
        return n - len(self.__points)

    def updatePoint(self, idx: int, new_point: MyPoint):
        """
        Update a point at a specific index with new coordinates and color.

        Parameters:
            idx (int): The index of the point to update.
            new_point (MyPoint): The new point with updated data.

        Return:
            None
        """
        if not (0 <= idx < len(self.__points)):
            raise IndexError(f"Index {idx} out of range for update.")
        self.__points[idx].set_point(*new_point.get_point())
        self.__points[idx].set_color(new_point.get_color())

    def removePoint(self, idx: int):
        """
        Remove a point at a specific index.

        Parameters:
            idx (int): The index of the point to remove.

        Return:
            None
        """
        if not (0 <= idx < len(self.__points)):
            raise IndexError(f"Index {idx} out of range for removal.")
        self.__points.pop(idx)

    def plot(self):
        """
        Plot all points in the repository using matplotlib.

        Parameters:
            None

        Return:
            None
        """
        x = [point.get_point()[0] for point in self.__points]
        y = [point.get_point()[1] for point in self.__points]
        colors = [point.get_color() for point in self.__points]

        # Ensure colors are valid for matplotlib
        valid_colors = {"red", "green", "blue", "yellow", "magenta"}
        colors = [c if c in valid_colors else "black" for c in colors]

        plt.scatter(x, y, c=colors)
        plt.show()

    def getMaxDist(self) -> float:
        """
        Calculate the maximum distance between any two points in the repository.

        Parameters:
            None

        Return:
            (float): The maximum distance, or 0 if fewer than two points exist.
        """
        if len(self.__points) < 2:
            return 0

        ans = 0
        for i, point1 in enumerate(self.__points):
            for point2 in self.__points[i + 1 :]:
                ans = max(ans, self.__distance(point1, point2))
        return ans

    def shiftPointsY(self):
        """
        Shift all points to have an x-coordinate of 0.

        Parameters:
            None

        Return:
            None
        """
        for point in self.__points:
            point.set_x(0)

    def deleteAllInsideCircle(self, center: MyPoint, radius: int) -> int:
        """
        Remove all points inside a circle defined by a center and radius.

        Parameters:
            center (MyPoint): The center of the circle.
            radius (int): The radius of the circle.

        Return:
            (int): Number of points deleted
        """
        n = len(self.__points)
        self.__points = [
            point
            for point in self.__points
            if (self.__distance(center,point) > radius)
        ]
        
        return n - len(self.__points)


if __name__ == "__main__":
    repository = PointRepository()
    point = MyPoint(1, 2, "red")
    repository.addPoint(point)
    point = MyPoint(3, 2, "blue")
    repository.addPoint(point)
    point = MyPoint(3, 1, "green")
    repository.addPoint(point)
    point = MyPoint(1, 4, "red")
    repository.addPoint(point)
    point = MyPoint(4, 1, "yellow")
    repository.addPoint(point)

    print("Minimum Distance:", repository.minDistance())
    repository.plot()
