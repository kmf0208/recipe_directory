from lib.recipes import Recipes


def test_artist_constructs():
    recipes = Recipes(1, "cake1", 8, 3)
    assert recipes.id == 1
    assert recipes.title == "cake1"
    assert recipes.avg_cooking_time == 8
    assert recipes.rating == 3

def test_artists_format_nicely():
    artist = Recipes(1, "cake1", 8, 3)
    assert str(artist) == "recipes(1, cake1, 8, 3)"

def test_artists_are_equal():
    recipes1 = Recipes(1, "cake1", 8, 3)
    recipes2= Recipes(1, "cake1", 8, 3)
    assert recipes1 == recipes2