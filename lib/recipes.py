

class Recipes:
    def __init__(self, id, title, avg_cooking_time, rating):
        self.id = id
        self.title = title
        self.avg_cooking_time = avg_cooking_time
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"recipes({self.id}, {self.title}, {self.avg_cooking_time}, {self.rating})"