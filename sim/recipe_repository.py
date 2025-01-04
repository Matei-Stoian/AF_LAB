from recipe_class import Recipe
import random
class RecipeRepository:

    def __init__(self):
        self._recipies:list[Recipe] = []

    def add_recipe(self,id:int,name:str,cuisine:str,difficulty:int,preparation_time:int):
        if id is None or not isinstance(id,int):
            raise TypeError("Not the right id input.")
        if name is None or not isinstance(name,str):
            raise TypeError("Not the right name input.")
        if cuisine not in ["Italian","Mexican","Indian"] or not isinstance(cuisine,str):
            raise TypeError("Not the right cusine input.")
        if difficulty is None or not isinstance(difficulty,int):
            raise TypeError("Not the right difficulty input.")
        if preparation_time < 1 or not isinstance(preparation_time,int):
            raise TypeError("Not the right preparation_time input.")
        new_recipe = Recipe(id,name,cuisine,difficulty,preparation_time)
        self._recipies.append(new_recipe)
    
    def get_all(self):
        return self._recipies
    def update_by_id(self,id,preparation_time:int):
        if preparation_time < 1:
            raise ValueError("The preparation time must be greater then 1.")
        
        for recipe in self._recipies:
            if recipe.id == id:
                recipe.preparation_time(preparation_time)
    
    def delete_all_under_10_min(self):
        
        for i in range(len(self._recipies)-1,0,-1):
            if self._recipies[i].preparation_time < 10:
                self._recipies.pop(i)

    @staticmethod
    def quick_sort(nums, key=lambda x: x, comp=lambda x, y: x < y):
        if len(nums) <= 1:
            return nums
        pivot = key(nums[random.randint(0, len(nums) - 1)])
        left = [x for x in nums if comp(key(x), pivot)]
        middle = [x for x in nums if key(x) == pivot]
        right = [x for x in nums if comp(pivot, key(x))]
        return RecipeRepository.quick_sort(left, key, comp) + middle + RecipeRepository.quick_sort(right, key, comp)


    def sort_by_name(self):
        return RecipeRepository.quick_sort(self._recipies,key= lambda recipe: recipe.name)
    
    def sort_by_difficulty(self):
        return RecipeRepository.quick_sort(self._recipies,key= lambda recipie: recipie.difficulty,comp= lambda x,y: x>y)





    