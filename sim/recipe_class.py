class Recipe:

    def __init__(
        self, id: int, name: str, cuisine: str, difficulty: int, preparation_time: int
    ):
        self._id = id
        self._name = name
        self._cuisine = cuisine
        self._difficulty = difficulty
        self._preppartion_time = preparation_time

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def id(self, name: str):
        self._name = name

    @property
    def cuisine(self):
        return self._cuisine

    @cuisine.setter
    def cuisine(self, cuisine):
        self._cuisine = cuisine

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty: int):
        self._difficulty = difficulty

    @property
    def preparation_time(self):
        return self._preppartion_time

    @preparation_time.setter
    def preparation_time(self, preparation_time: int):
        self._preppartion_time = preparation_time
    
    def __repr__(self):
        return f"Recipie with id:{self._id},name:{self._name},cuisine:{self._cuisine},difficulry:{self._difficulty},preparation_time:{self._preppartion_time}"
