# from storagejson_storage import JsonStorage
# from movie_app import MovieApp

# def main():
#     """
#     Start point of the program.
#     Creates the storage service and starts the MovieApp.
#     """
#     storage = JsonStorage("data/movies.json")
#     app = MovieApp(storage)
#     app.run()

# if __name__ == "__main__":
#     main()

from storage.json_storage import JsonStorage
from storage.csv_storage import CsvStorage
from movie_app import MovieApp

def main():
    # Use JSON storage:
    # storage = JsonStorage("data/movies.json")
    # Or use CSV storage:
    storage = CsvStorage("data/movies.csv")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
