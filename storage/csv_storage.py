import csv
import os
from storage.istorage import IStorage


class CsvStorage(IStorage):
    """
    This class implements the IStorage interface and stores movie data in a CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes a new CsvStorage instance.

        Parameters:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path

        # Create the file with headers if it does not exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["title", "rating", "year", "poster"])

    def list_movies(self):
        """
        Reads all movies from the CSV file and returns them as a dictionary.

        Returns:
            dict: Movies in the format {
                "Title": {
                    "year": int,
                    "rating": float,
                    "poster": str
                }
            }
        """
        movies = {}
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row["title"]
                movies[title] = {
                    "rating": float(row["rating"]),
                    "year": int(row["year"]),
                    "poster": row["poster"]
                }
        return movies

    def add_movie(self, title, year, rating, poster_url):
        """
        Adds a new movie to the CSV file.

        Parameters:
            title (str): Title of the movie
            year (int): Year of release
            rating (float): Rating
            poster_url (str): Link to the poster image
        """
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, rating, year, poster_url])

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file based on its title.

        Parameters:
            title (str): Title of the movie to delete
        """
        movies = self.list_movies()
        # Case-insensitive title matching
        title_map = {k.lower(): k for k in movies.keys()}
        if title.lower() in title_map:
            del movies[title_map[title.lower()]]
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["title", "rating", "year", "poster"])
                for t, details in movies.items():
                    writer.writerow([t, details["rating"], details["year"], details["poster"]])

    def update_movie(self, title, new_rating):
        """
        Updates the rating of a movie in the CSV file.

        Parameters:
            title (str): Title of the movie
            new_rating (float): New rating to be stored
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = new_rating
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["title", "rating", "year", "poster"])
                for t, details in movies.items():
                    writer.writerow([t, details["rating"], details["year"], details["poster"]])