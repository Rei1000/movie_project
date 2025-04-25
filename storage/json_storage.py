import json
import os
from storage.istorage import IStorage


class JsonStorage(IStorage):
    """
    This class stores and loads movie data from a JSON file.
    It implements all methods from the IStorage interface and can be used as a storage solution.
    """

    def __init__(self, file_path):
        """
        Creates a new instance of the JSON storage.

        Parameters:
            file_path (str): Path to the JSON file where the data is stored.
        """
        self.file_path = file_path

        # If the file does not exist, create it as an empty dictionary
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def _load_data(self):
        """
        Helper method: Loads data from the JSON file.

        Returns:
            dict: The loaded movie data
        """
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _save_data(self, data):
        """
        Helper method: Saves data to the JSON file.

        Parameters:
            data (dict): The movie data to be saved
        """
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def list_movies(self):
        """
        Returns all movies from the JSON file.

        Returns:
            dict: All movies with the title as key
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster_url):
        """
        Adds a new movie to the JSON file.

        Parameters:
            title (str): Title of the movie
            year (int): Year of release
            rating (float): Rating
            poster_url (str): Link to the poster image
        """
        data = self._load_data()
        data[title] = {
            "year": year,
            "rating": rating,
            "poster": poster_url
        }
        self._save_data(data)

    def delete_movie(self, title):
        """
        Removes a movie from the JSON file.

        Parameters:
            title (str): Title of the movie to delete
        """
        data = self._load_data()
        # Case-insensitive title matching
        title_map = {k.lower(): k for k in data.keys()}
        if title.lower() in title_map:
            del data[title_map[title.lower()]]
            self._save_data(data)

    def update_movie(self, title, new_rating):
        """
        Updates the rating of a movie.

        Parameters:
            title (str): Title of the movie
            new_rating (float): New rating to store
        """
        data = self._load_data()
        if title in data:
            data[title]["rating"] = new_rating
            self._save_data(data)