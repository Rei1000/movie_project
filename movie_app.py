import os
os.makedirs("_static", exist_ok=True)
import random
from omdb_api import fetch_movie_from_api

class MovieApp:
    """
    This class contains the main logic of the MovieApp:
    Menu navigation, user commands, and interaction with the storage system.

    It uses a storage object that implements the IStorage interface.
    """

    def __init__(self, storage) -> None:
        """
        Creates a new MovieApp instance.

        Parameters:
            storage: An object that implements the IStorage interface (e.g., JsonStorage)
        """
        self._storage = storage

    def _list_all_movies(self) -> None:
        """
        Retrieves all stored movies from the storage and displays them in the console.
        """
        movies = self._storage.list_movies()

        if not movies:
            print("No movies found in storage.")
            return

        print("\nYour Movies:")
        print("-" * 30)
        for title, details in movies.items():
            print(f"Title: {title}")
            print(f"  Year: {details.get('year')}")
            print(f"  Rating: {details.get('rating')}")
            print(f"  Poster URL: {details.get('poster')}")
            print("-" * 30)

    def _add_movie(self) -> None:
        """
        Adds a movie by fetching its data from OMDb API.
        Only requires the movie title from the user.
        """
        title = input("Enter movie title: ")
        movie = fetch_movie_from_api(title)

        if movie:
            self._storage.add_movie(
                movie["title"],
                movie["year"],
                movie["rating"],
                movie["poster"]
            )
            print(f"Movie '{movie['title']}' added successfully!")
        else:
            print(f"Movie '{title}' not found in database.")

    def _update_movie(self) -> None:
        """
        Prompts the user for a movie title and a new rating,
        then updates the movie's rating using the storage.
        """
        title = input("Enter the title of the movie to update: ")
        movies = self._storage.list_movies()
        title_map = {k.lower(): k for k in movies.keys()}

        if title.lower() in title_map:
            original_title = title_map[title.lower()]
            while True:
                try:
                    new_rating = float(input("Enter the new rating (0.0 - 10.0): "))
                    if 0.0 <= new_rating <= 10.0:
                        self._storage.update_movie(original_title, new_rating)
                        print(f"Movie '{original_title}' updated successfully!")
                        break
                    else:
                        print("Rating must be between 0.0 and 10.0")
                except ValueError:
                    print("Invalid input. Rating must be a number.")
        else:
            print(f"Movie '{title}' not found.")

    def _delete_movie(self) -> None:
        """
        Prompts the user for a movie title and deletes the movie using the storage.
        """
        title = input("Enter the title of the movie to delete: ")
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully!")

    def _add_movie_from_api(self):
        """
        Prompts the user for a movie title, fetches the data from OMDb API,
        and adds the movie to the storage if found.
        """
        title = input("Enter the title of the movie to fetch from OMDb: ")
        movie = fetch_movie_from_api(title)

        if movie:
            self._storage.add_movie(movie["title"], movie["year"], movie["rating"], movie["poster"])
            print(f"✅ Movie '{movie['title']}' added successfully from API!")
        else:
            print("❌ Could not add the movie. Please try again with a different title.")

    def _stats(self) -> None:
        """
        Shows statistics about the movies in the database:
        - Average rating
        - Best and worst rated movies
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in database.")
            return

        ratings = [movie["rating"] for movie in movies.values()]
        average = sum(ratings) / len(ratings)
        max_rating = max(ratings)
        min_rating = min(ratings)

        best_movies = [title for title, movie in movies.items() if movie["rating"] == max_rating]
        worst_movies = [title for title, movie in movies.items() if movie["rating"] == min_rating]

        print(f"\nAverage rating: {average:.2f}")
        print(f"Best movies ({max_rating}): {', '.join(best_movies)}")
        print(f"Worst movies ({min_rating}): {', '.join(worst_movies)}")

    def _random_movie(self) -> None:
        """
        Displays a random movie from the database.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in database.")
            return
        try:
            title, movie = random.choice(list(movies.items()))
            year = movie.get('year', 'N/A')
            rating = movie.get('rating', 'N/A')
            print(f"Random movie: {title} ({year}) - Rating: {rating}")
        except Exception as e:
            print(f"Error selecting a random movie: {e}")

    def _movies_sorted_by_rating(self) -> None:
        """
        Displays all movies sorted by rating (descending).
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in database.")
            return
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
        print("\nMovies sorted by rating:")
        for title, movie in sorted_movies:
            print(f"{title}: {movie['rating']} ({movie['year']})")

    def _generate_website(self) -> None:
        """
        Generates a website from the movies in the database using the template files.
        Creates an index.html file with the movie grid and copies the required CSS.
        """
        import shutil

        # Load the template file
        try:
            with open("_static/index_template.html", "r") as file:
                template = file.read()
        except FileNotFoundError:
            print("Template file not found in _static directory.")
            return

        # Copy the CSS file to the main directory
        try:
            shutil.copy2("_static/style.css", "style.css")
        except FileNotFoundError:
            print("Style file not found in _static directory.")
            return
        except Exception as e:
            print(f"Error copying CSS file: {str(e)}")
            return

        # Get all movies from storage
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found in storage.")
            return

        # Create the movie grid
        movie_grid = ""
        for title, movie in movies.items():
            movie_grid += f"""
            <li class="movie-item">
                <div class="movie-poster">
                    <img class="movie-poster-img" src="{movie.get('poster', '')}" alt="{title} Poster"/>
                </div>
                <div class="movie-title">{title}</div>
                <div class="movie-year">{movie.get('year', 'N/A')}</div>
                <div class="movie-rating">Rating: {movie.get('rating', 'N/A')}/10</div>
            </li>"""

        # Replace placeholders in the template
        website_content = template.replace("__TEMPLATE_TITLE__", "Reiner's Movie Collection")
        website_content = website_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

        # Save the generated website
        try:
            with open("index.html", "w") as file:
                file.write(website_content)
            print("Website was generated successfully.")
        except Exception as e:
            print(f"Error generating website: {str(e)}")

    def run(self) -> None:
        """
        Starts the main menu of the application.
        Asks the user for a command and calls the appropriate method.
        """
        while True:
            print("\nMovie App Menu")
            print("1. List all movies")
            print("2. Add a movie")
            print("3. Update a movie")
            print("4. Delete a movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Movies sorted by rating")
            print("8. Generate website")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self._list_all_movies()
            elif choice == "2":
                self._add_movie()
            elif choice == "3":
                self._update_movie()
            elif choice == "4":
                self._delete_movie()
            elif choice == "5":
                self._stats()
            elif choice == "6":
                self._random_movie()
            elif choice == "7":
                self._movies_sorted_by_rating()
            elif choice == "8":
                self._generate_website()
            elif choice == "9":
                print("Exiting the Movie App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-9.")