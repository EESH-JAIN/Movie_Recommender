# Movie Recommender

This project is a movie recommendation system built using Python, Pandas, scikit-learn, and Streamlit. It recommends movies based on user preferences, using content-based filtering and fuzzy matching.

## Features

* **Genre-based Recommendations:** Users can select a genre and receive recommendations within that genre.
* **Content-based Filtering:** Recommendations are based on the similarity of movie overviews.
* **Fuzzy Matching:** Handles variations in movie titles entered by the user.
* **Movie Details:** Displays movie titles, descriptions, and ratings.
* **Multiple Recommendations:** Shows the top 3 recommended movies.
* **Regenerate Functionality:** Allows users to get a new recommendation.
* **Movie Search:** Users can search for specific movies.

## Technologies Used

* Python
* Pandas
* scikit-learn (TfidfVectorizer, cosine_similarity)
* Streamlit
* fuzzywuzzy

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

    (Replace `<repository_url>` with the URL of your repository.)

2.  **Navigate to the project directory:**

    ```bash
    cd movie-recommender
    ```

3.  **Install the required libraries:**

    ```bash
    pip install pandas scikit-learn streamlit fuzzywuzzy
    ```

4.  **Download the dataset:**
    * Download `tmdb_5000_movies.csv` from Kaggle or where ever you got it, and place it in the same directory as `movie_recommender.py`.

## Usage

1.  **Run the Streamlit app:**

    ```bash
    streamlit run movie_recommender.py
    ```

2.  **Open the app in your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

3.  **Use the app:**
    * Select a genre from the dropdown menu.
    * Enter 2-3 movies you like, separated by commas.
    * View the recommended movies, along with their descriptions and ratings.
    * Use the "Regenerate" button to get a new recommendation.
    * Use the search bar to look up specific movies.

## Dataset

* The project uses the `tmdb_5000_movies.csv` dataset, which contains information about movies from The Movie Database (TMDB).

## Future Improvements

* Implement collaborative filtering for personalized recommendations.
* Integrate movie posters using the TMDB API.
* Add user reviews and ratings.
* Enhance the UI with more styling and features.
* Deploy the application to a cloud platform.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, feel free to open an issue or submit a pull request.
