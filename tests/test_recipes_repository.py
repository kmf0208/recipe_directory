from lib.recipes import Recipes
from lib.recipes_repository import RecipeRepository



def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new ArtistRepository

    artists = repository.all() # Get all artists

    # Assert on the results
    result = repository.all()
    assert result == [
        Recipes(1, 'cake1', 8, 3),
        Recipes(2, 'cake2', 7, 4),
        Recipes(3, 'cake3', 4, 1)]
    


def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection)

    artist = repository.find(3)
    assert artist == Recipes(3, 'cake3', 4, 1)