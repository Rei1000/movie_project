# from json_storage import JsonStorage
# from movie_app import MovieApp

# def main():
#     """
#     Start point of the program.
#     Creates the storage service and starts the MovieApp.
#     """
#     storage = JsonStorage("movies.json")
#     app = MovieApp(storage)
#     app.run()

# if __name__ == "__main__":
#     main()

from csv_storage import CsvStorage
from movie_app import MovieApp

def main():
    storage = CsvStorage("movies.csv")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
