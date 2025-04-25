from abc import ABC, abstractmethod

class IStorage(ABC):
    """
    This is an interface (abstract base class) that defines
    which methods all storage classes (e.g., JSON, CSV) must implement.

    The advantage: we can easily switch the storage type
    without changing the rest of the program.
    """

    @abstractmethod
    def list_movies(self):
        """
        Returns all movies as a dictionary.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url):
        """
        Adds a new movie to the storage.

        Parameters:
            title (str): The title of the movie
            year (int): The release year
            rating (float): A rating between 0.0 and 10.0
            poster_url (str): A URL to the movie poster
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the storage by its title.
        """
        pass

    @abstractmethod
    def update_movie(self, title, new_rating):
        """
        Updates the rating of a movie.

        Parameters:
            title (str): The title of the movie
            new_rating (float): The new rating
        """
        pass