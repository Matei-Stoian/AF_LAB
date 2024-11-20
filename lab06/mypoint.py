class MyPoint:

    def __init__(self, coord_x:float, coord_y:float, color:str):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        if color not in ["red", "green", "blue", "yellow", "magenta",None]:
            raise Exception("Not a valid color")
        else:
            self.__color = color

    def get_point(self) -> tuple[float, float]:
        return (self.__coord_x, self.__coord_y)

    def get_x(self) -> float:
        return self.__coord_x
    def get_y(self) -> float:
        return self.__coord_y
    def set_point(self, coord_x: float, coord_y: float):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
    def set_x(self,x:float):
        self.__coord_x = x

    def set_y(self,y:float):
        self.__coord_y = y

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str):
        if color not in ["red", "green", "blue", "yellow", "magenta"]:
            raise Exception("Not a vlid color")
        else:
            self.__color = color

    def __str__(self):
        return f"Point ({self.__coord_x},{self.__coord_y}) of color {self.__color}"
    
    def __eq__(self, other):
        if isinstance(other, MyPoint):
            return self.__coord_x == other.get_x() and self.__coord_y == other.get_y() and self.__color == other.get_color()
        return False
    
    def __repr__(self):
        return f"MyPoint({self.__coord_x}, {self.__coord_x}, '{self.__color}')"
