import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender")

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommendation System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_names = []

    for i in recommended_movies:
        recommended_names.append(movies.iloc[i[0]].title)

    return recommended_names

if st.button("Show Recommendations"):
    names = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for name in names:
        st.write("- " + name)
