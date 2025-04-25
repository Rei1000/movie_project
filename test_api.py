from omdb_api import fetch_movie_from_api

# Replace this with any movie title you want to test
title = input("Enter movie title to search: ")

movie_data = fetch_movie_from_api(title)

if movie_data:
    print("\n✅ Movie found!")
    print(f"Title:  {movie_data['title']}")
    print(f"Year:   {movie_data['year']}")
    print(f"Rating: {movie_data['rating']}")
    print(f"Poster: {movie_data['poster']}")
else:
    print("❌ Movie could not be fetched.")