# Movie Project

A modern, console-based Python application for managing your personal movie collection, featuring OMDb API integration and automatic website generation.

## Features

- **Add Movies via OMDb API:**  
  Add movies by simply entering the title. The app fetches year, rating, and poster automatically from the OMDb API.

- **List, Update, and Delete Movies:**  
  View all movies, update ratings, or remove entries from your collection.

- **Statistics:**  
  Get insights into your collection: average rating, best and worst movies, and more.

- **Random Movie Picker:**  
  Let the app suggest a random movie from your collection.

- **Sort by Rating:**  
  Display all movies sorted by their rating.

- **Generate a Stylish Website:**  
  Create a responsive HTML website of your movie collection with one command. The site includes movie posters, ratings, and years, styled with CSS.

- **Persistent Storage:**  
  Choose between JSON or CSV file storage for your data.

## Technologies Used

- **Python 3.10+**
- [requests](https://pypi.org/project/requests/) – for OMDb API access
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for environment variable management
- **Standard Library:** os, random, json, csv, shutil

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rei1000/movie_project.git
   cd movie_project
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OMDb API key:**
   - Register for a free API key at [OMDb API](https://www.omdbapi.com/apikey.aspx)
   - Create a `.env` file in the project root:
     ```
     OMDB_API_KEY=your_api_key_here
     ```

## Usage

Start the application:
```bash
python main.py
```

Follow the menu to add, list, update, or delete movies, view stats, pick a random movie, sort by rating, or generate your website.

### Example: Generate Website

After adding movies, select the "Generate website" option in the menu.  
The app will create an `index.html` and a `style.css` in your project folder.  
Open `index.html` in your browser to view your collection.

## Project Structure

```
movie_project/
│
├── main.py
├── movie_app.py
├── omdb_api.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── data/
│   ├── movies.json
│   └── movies.csv
│
├── storage/
│   ├── json_storage.py
│   ├── csv_storage.py
│   └── istorage.py
│
├── static/
│   ├── index_template.html
│   └── style.css
│
└── ...
```

## Object-Oriented Design

This project demonstrates key OOP principles:

- **Abstraction & Interfaces:**  
  The `IStorage` abstract base class defines a common interface for all storage backends.

- **Inheritance:**  
  Both `JsonStorage` and `CsvStorage` inherit from `IStorage` and provide concrete implementations.

- **Polymorphism:**  
  The main application (`MovieApp`) interacts with any storage class that implements the `IStorage` interface, making it easy to switch storage types.

- **Encapsulation:**  
  Data storage logic is encapsulated in dedicated classes, keeping the main application logic clean and modular.

- **API Integration:** 
  Demonstrates working with real-world APIs and error handling.

- **File I/O:** 
  Shows robust data persistence with both JSON and CSV.

- **Separation of Concerns:** 
  Clean code structure with interfaces and modular design.

- **Automation:** 
  Website generation from data.

- **User Experience:** 
  Intuitive menu and clear feedback.

---

**Created by [Rei1000](https://github.com/Rei1000)**
