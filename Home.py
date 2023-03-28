import streamlit as st
import pickle
import requests
from collections.abc import MutableMapping

st.title("Recommender System")
col1, col2 = st.columns(2)
with col1:
    st.header("Popular Books")
with col2:
    st.header("Popular Movies")

st.cache(persist=True)
def load_data():
    books = pickle.load(open('dataset/books.pkl', 'rb'))
    similarity_scores = pickle.load(open('dataset/similarity_books.pkl', 'rb'))
    popular_df = pickle.load((open('dataset/popular.pkl', 'rb')))
    movies = pickle.load(open('dataset/movie_pop.pkl', 'rb'))
    similarity = pickle.load(open('dataset/similarity_movies.pkl', 'rb'))

    return books,similarity_scores,popular_df,movies,similarity

books, similarity_score, popular_df,movies,similarity = load_data()



st.cache(persist=True)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.cache(persist=True)
def showdata():
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        for i in range(0,24):
            st.image(popular_df.iloc[[i][0]].Img_url)
            st.write(popular_df.iloc[[i][0]].Book_Title)
    with col2:
        for i in range(27,50):
            st.image(popular_df.iloc[[i][0]].Img_url)
            st.write(popular_df.iloc[[i][0]].Book_Title)
    with col3:
        for i in range(1,20):
            movie_id = movies.iloc[[i][0]].movie_id
            st.image(fetch_poster(movie_id))
            st.write(movies.iloc[[i][0]].title)
    with col4:
        for i in range(21,40):
            movie_id = movies.iloc[[i][0]].movie_id
            st.image(fetch_poster(movie_id))
            st.write(movies.iloc[[i][0]].title)

showdata = showdata()










