import streamlit as st
import pickle
import numpy as np
import requests

st.cache(persist=True)
def load_data():
    movies = pickle.load(open('dataset/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('dataset/similarity_movies.pkl', 'rb'))

    return movies,similarity
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_tags = []
    recommended_movie_posters = []
    recommended_movie_ratings = []
    recommended_movie_similarity = []
    for i in distances[0:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_tags.append(movies.iloc[i[0]].tags)
        recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)
        recommended_movie_similarity.append(int(i[1]*100))

    return recommended_movie_names, recommended_movie_tags, recommended_movie_posters,recommended_movie_ratings,recommended_movie_similarity
def filterByCrew(crew):
    # index fetch
    index = movies[movies['crew'] == crew].duplicated('crew').sum()
    st.write('Total number of movies : {}'.format(index+1))
    index_books = []
    for i in range(index+1):
        index_books.append(movies[movies['crew'] == crew].index[i])
    filter_movie_name = []
    filter_movie_poster = []
    filter_movie_rating = []
    filter_movie_crew = []
    for j in range(index+1):
        movie_id = movies.iloc[[index_books[j]][0]].movie_id
        filter_movie_poster.append(fetch_poster(movie_id))
        filter_movie_name.append(movies.iloc[[index_books[j]][0]].title)
        filter_movie_rating.append(movies.iloc[[index_books[j]][0]].vote_average)
        filter_movie_crew.append(movies.iloc[[index_books[j]][0]].crew)
    return filter_movie_name,filter_movie_poster,filter_movie_rating,filter_movie_crew
st.title('🎥Movie Recommender System')

movies,similarity = load_data()

tab1, tab2 = st.tabs(["Recommender System", "Filter By Crew"])


with tab1:
    st.header("Recommender System")




    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation movies'):
        recommended_movie_names, recommended_movie_tags, recommended_movie_posters,recommended_movie_ratings,recommended_movie_similarity = recommend(selected_movie)

        col1, col2, col3,col4 = st.columns(4)
        with col1:
            st.image(recommended_movie_posters[0])
            st.write(recommended_movie_names[0])
            st.caption("Rating : {}".format(recommended_movie_ratings[0]))
        with col2:
            st.image(recommended_movie_posters[1])
            st.write(recommended_movie_names[1])
            st.caption("Rating : {}".format(recommended_movie_ratings[1]))
            st.caption("similarity about :{} %".format(recommended_movie_similarity[1]))
        with col3:
            st.image(recommended_movie_posters[2])
            st.write(recommended_movie_names[2])
            st.caption("Rating : {}".format(recommended_movie_ratings[2]))
            st.caption("similarity about :{} %".format(recommended_movie_similarity[2]))
        with col4:
            st.image(recommended_movie_posters[3])
            st.write(recommended_movie_names[3])
            st.caption("Rating : {}".format(recommended_movie_ratings[3]))
            st.caption("similarity about :{} %".format(recommended_movie_similarity[3]))
    col1, col2, col3,col4 = st.columns(4)
    with col1:

        if st.button('overview'):
            recommended_movie_names, recommended_movie_tags, recommended_movie_posters, recommended_movie_ratings,recommended_movie_similarity = recommend(selected_movie)
            st.write(recommended_movie_names[0])
            st.caption(recommended_movie_tags[0])
    with col2:
        if st.button('overview '):
            recommended_movie_names, recommended_movie_tags, recommended_movie_posters, recommended_movie_ratings,recommended_movie_similarity = recommend(selected_movie)
            st.write(recommended_movie_names[1])
            st.caption(recommended_movie_tags[1])
    with col3:
        if st.button('overview  '):
            recommended_movie_names, recommended_movie_tags, recommended_movie_posters, recommended_movie_ratings,recommended_movie_similarity = recommend(selected_movie)
            st.write(recommended_movie_names[2])
            st.caption(recommended_movie_tags[2])
    with col4:
        if st.button('overview   '):
            recommended_movie_names, recommended_movie_tags, recommended_movie_posters, recommended_movie_ratings,recommended_movie_similarity = recommend(selected_movie)
            st.write(recommended_movie_names[3])
            st.caption(recommended_movie_tags[3])
with tab2:
    st.header("Filter")

    crew_list = movies['crew'].values
    selected_crew = st.selectbox("Type or select a movie from the dropdown",crew_list)
    if st.button('filtering'):
        filter_movie_name,filter_movie_poster,filter_movie_rating,filter_movie_crew = filterByCrew(selected_crew)
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.image(filter_movie_poster[0])
            st.write(filter_movie_name[0])
            st.caption(filter_movie_crew[0])
            st.caption('Rating {}'.format(round(filter_movie_rating[0], 2)))
        with col2:
            st.image(filter_movie_poster[1])
            st.write(filter_movie_name[1])
            st.caption(filter_movie_crew[1])
            st.caption('Rating {}'.format(round(filter_movie_rating[1], 2)))
        with col3:
            st.image(filter_movie_poster[2])
            st.write(filter_movie_name[2])
            st.caption(filter_movie_crew[2])
            st.caption('Rating {}'.format(round(filter_movie_rating[2], 2)))
        with col4:
            st.image(filter_movie_poster[3])
            st.write(filter_movie_name[3])
            st.caption(filter_movie_crew[3])
            st.caption('Rating {}'.format(round(filter_movie_rating[3], 2)))

