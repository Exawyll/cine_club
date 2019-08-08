import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    with open(DATA_FILE, "r") as f:
        list_string = json.load(f)

    list_movies = [Movie(movie) for movie in list_string]

    return list_movies

class Movie:

    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà présent dans la liste !")
            return False
    
    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
    

if __name__ == "__main__":
    m = Movie('lotr')
    m.add_to_movies()
    m = Movie('harry potter')
    m.add_to_movies()
    m = Movie('L\'arme fatale 4')
    m.add_to_movies()
    m = Movie('lotr')
    m.add_to_movies()
    print(get_movies())