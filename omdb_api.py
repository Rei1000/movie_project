import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_movie_from_api(title):
    """
    Fetches movie data from the OMDb API using the given title.

    Parameters:
        title (str): The title of the movie to search for.

    Returns:
        dict: Movie data including title, year, rating, and poster URL,
              or None if the movie is not found or an error occurs.
    """
    api_key = os.getenv("OMDB_API_KEY")

    if not api_key:
        print("API key is missing. Please check your .env file.")
        return None

    if not title or not isinstance(title, str):
        print("Invalid movie title provided.")
        return None

    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        if data.get("Response") == "True":
            # Use fallback values to ensure valid formatting
            title = data.get("Title", "Unknown Title")
            year = int(data.get("Year", 0))
            imdb_rating = data.get("imdbRating", "0.0")
            rating = float(imdb_rating) if imdb_rating != "N/A" else 0.0
            poster = data.get("Poster", "")

            return {
                "title": title,
                "year": year,
                "rating": rating,
                "poster": poster
            }
        else:
            print(f"Movie not found: {data.get('Error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError as ve:
        print(f"Error processing data: {ve}")
        return None