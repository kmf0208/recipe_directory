from lib.recipes import Recipes

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipe = []
        for row in rows:
            item = Recipes(row["id"], row["title"], row["avg_cooking_time"], row["rating"])
            recipe.append(item)
        return recipe
    
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [artist_id])
        row = rows[0]
        return Recipes(row["id"], row["title"], row["avg_cooking_time"], row["rating"])
    