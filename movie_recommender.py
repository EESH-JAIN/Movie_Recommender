import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from fuzzywuzzy import process

# Load and preprocess data
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['overview'] = df['overview'].fillna('')
    df['genres'] = df['genres'].apply(ast.literal_eval)
    df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in x])
    return df

# Create TF-IDF vectors
def create_tfidf(df, feature_column):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df[feature_column])
    return tfidf, tfidf_matrix

# Calculate cosine similarity
def calculate_similarity(tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

# Get movie recommendations
def get_recommendations(df, similarity_matrix, liked_movies, genre, watched_movies, num_recommendations=3):
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    movie_titles = df['title'].tolist()

    matched_indices = []
    for movie in liked_movies:
        match, score = process.extractOne(movie, movie_titles)
        if score >= 70:
            matched_indices.append(indices[match])
        else:
            st.warning(f"Could not find a close match for '{movie}'. Please check the title.")
            return None

    if not matched_indices:
        return None

    similarity_scores = similarity_matrix[matched_indices].mean(axis=0)
    similar_movies = list(enumerate(similarity_scores))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    recommendations = []
    count = 0
    for i, score in similar_movies:
        if df['genres'].iloc[i] and genre in df['genres'].iloc[i] and df['title'].iloc[i] not in watched_movies and df['title'].iloc[i] not in liked_movies and count < num_recommendations:
            recommendations.append(i)
            count +=1

    return recommendations

# Streamlit app
def main():
    st.title("Movie Recommender")

    df = load_data("tmdb_5000_movies.csv")
    tfidf, tfidf_matrix = create_tfidf(df, 'overview')
    similarity_matrix = calculate_similarity(tfidf_matrix)

    genre = st.selectbox("Select Genre", ['Action', 'Comedy', 'Drama', 'Thriller', 'Romance'])
    liked_movies = st.text_input("Enter 2-3 liked movies (comma-separated)").split(',')
    liked_movies = [movie.strip() for movie in liked_movies if movie.strip()]

    if 'watched_movies' not in st.session_state:
        st.session_state['watched_movies'] = []

    if liked_movies:
        recommendation_indices = get_recommendations(df, similarity_matrix, liked_movies, genre, st.session_state['watched_movies'])

        if recommendation_indices:
            st.subheader("Recommended Movies:")
            for index in recommendation_indices:
                recommended_movie = df.iloc[index]
                st.write(f"**{recommended_movie['title']}** (Rating: {recommended_movie['vote_average']})")
                st.write(f"Description: {recommended_movie['overview']}")
                if st.button(f"Regenerate {recommended_movie['title']}"):
                    st.session_state['watched_movies'].append(recommended_movie['title'])
                    recommendation_indices.remove(index)
                    if recommendation_indices:
                        st.rerun()
                    else:
                        st.write("No more recommendations.")
                    break
        else:
            st.write("No recommendations found.")

    st.subheader("Search for a movie:")
    search_term = st.text_input("Enter movie title:")
    if search_term:
        match, score = process.extractOne(search_term, df['title'].tolist())
        if score >= 70:
            movie = df[df['title'] == match].iloc[0]
            st.write(f"**{movie['title']}** (Rating: {movie['vote_average']})")
            st.write(f"Description: {movie['overview']}")
        else:
            st.warning("Movie not found.")

if __name__ == "__main__":
    main()