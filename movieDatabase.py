import random


def menue():
    print("Reiner's Movie Database")
    menue_list = [
        "1.List movies",
        "2.Add movie",
        "3.Delete movie",
        "4.Update movie",
        "5.Stats",
        "6.Random movie",
        "7.Search movie",
        "8.Movies sorted by rating",
        "9.Exit"
    ]
    for option in menue_list:
        print(option)
    while True:
        try:
            choice = int(input("Enter choice (1-9): "))
            if 1 <= choice <= 9:
                return choice

            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input. Try again.")


def list_movies(movies):
    if not movies:
        print("No movies in the database")
        return
    print(f" {len(movies)} movies total")
    for name, rating in movies.items():
        print(f"{name}: {rating}")


def add_movie(movies):
    name = input("Enter movie name: ").strip()
    if name in movies:
        print("Movie already exists.")
        return
    try:
        rating = float(input("Enter movie rating (0.0 - 10.0): "))
        if 0.0 <= rating <= 10.0:
            movies[name] = rating
            print(f"Movie '{name}' added with {rating}.")
        else:
            print("rating must be between 0.0 and 10.0")
    except ValueError:
        print("Invalid input. Try again.")


def delete_movie(movies):
    if not movies:
        print("No movies in Database.")
        return
    list_movies(movies)
    name = input("Enter the name of the movie to delete: ").strip()
    if name in movies:
        del movies[name]
        print(f"Movie '{name}' deleted.")
    else:
        print("Movie not found")


def update_movie(movies):
    if not movies:
        print("No movies in Database..")
        return
    list_movies(movies)
    name = input("Enter the name of the movie to update: ").strip()
    if name in movies:
        try:
            rating = float(input("Enter new rating (0.0 - 10.0): "))
            if 0.0 <= rating <= 10.0:
                movies[name] = rating
                print(f" Movie '{name}' updated to rating {rating}.")
            else:
                print("Rating must be between 0.0 and 10.0")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Movie not found")


def stats(movies):
    if not movies:
        print("No movies in Database.")
        return

    ratings_list = list(movies.values())

    average = sum(ratings_list) / len(ratings_list)
    print(f"Average Rating: {average}")

    max_rating = max(ratings_list)
    best_movies = []

    min_rating = min(ratings_list)
    worst_movies = []

    for name, rating in movies.items():
        if rating == max_rating:
            best_movies.append(name)
        if rating == min_rating:
            worst_movies.append(name)

    print(f" Best Movies: {best_movies} Rating: {max_rating}")
    print(f" Worst Movies: {worst_movies} Rating: {min_rating}")


def random_movie(movies):
    if not movies:
        print("No movies in Database.")
        return
    name, rating = random.choice(list(movies.items()))
    print(f"Random movie: {name} Rating: {rating}")


def search_movie(movies):
    if not movies:
        print("No movies in Database.")
        return
    search_term = input("Enter part of the movie name to search: ").strip().lower()

    matches = [name for name in movies if search_term in name.lower()]

    if matches:
        print("Search results:")
        for name in matches:
            print(f"{name}: {movies[name]}")
    else:
        print("No matching movies found.")


def movies_sorted_by_rating(movies):
    if not movies:
        print("No movies in Database.")
        return
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    print("Movies sorted by rating:")
    for name, rating in sorted_movies:
        print(f"{name}: {rating}")


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }
    while True:

        choice = menue()
        if choice == 9:  # Zum Beenden
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            list_movies(movies)
        elif choice == 2:
            add_movie(movies)
        elif choice == 3:
            delete_movie(movies)
        elif choice == 4:
            update_movie(movies)
        elif choice == 5:
            stats(movies)
        elif choice == 6:
            random_movie(movies)
        elif choice == 7:
            search_movie(movies)
        elif choice == 8:
            movies_sorted_by_rating(movies)


if __name__ == "__main__":
    main()


