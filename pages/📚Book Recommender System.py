import streamlit as st
import pickle
import numpy as np
import requests

st.title('📚Books Reccomender System')

st.cache(persist=True)
def load_data():
    books = pickle.load(open('dataset/books_main.pkl', 'rb'))
    books_list = pickle.load(open('dataset/books_list.pkl', 'rb'))
    similarity_scores = pickle.load(open('dataset/similarity_books.pkl', 'rb'))
    popular_df = pickle.load((open('dataset/popular.pkl', 'rb')))
    book_author = pickle.load((open('dataset/book_author.pkl','rb')))

    return books,similarity_scores,popular_df,book_author,books_list

books, similarity_scores, popular_df,book_author,books_list= load_data()

st.cache(persist=True)
def recommendbooks(book):
    # index fetch
    index = books[books['Book_Title'] == book].index[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)

    recommended_book_name = []
    recommended_book_poster = []
    recommended_book_rating = []
    recommended_book_author = []
    recommended_book_similarity= []
    for i in similar_items[0:11]:
        recommended_book_name.append(books.iloc[i[0]].Book_Title)
        recommended_book_poster.append(books.iloc[i[0]].Img_url)
        recommended_book_rating.append(books.iloc[i[0]].avg_ratings)
        recommended_book_author.append(books.iloc[i[0]].Book_Author)
        recommended_book_similarity.append(int(i[1] * 100))


    return recommended_book_name,recommended_book_poster,recommended_book_rating,recommended_book_author,recommended_book_similarity
def filterByAuthor(author):
    # index fetch
    index = books[books['Book_Author'] == author].duplicated('Book_Author').sum()
    st.write('Total number of books : {}'.format(index+1))
    index_books = []
    for i in range(index+1):
        index_books.append(books[books['Book_Author'] == author].index[i])
    filter_book_name = []
    filter_book_poster = []
    filter_book_rating = []
    filter_book_author = []
    for j in range(index+1):
        filter_book_name.append(books.iloc[[index_books[j]][0]].Book_Title)
        filter_book_poster.append(books.iloc[[index_books[j]][0]].Img_url)
        filter_book_rating.append(books.iloc[[index_books[j]][0]].avg_ratings)
        filter_book_author.append(books.iloc[[index_books[j]][0]].Book_Author)
    return filter_book_name,filter_book_poster,filter_book_rating,filter_book_author



book_list = books_list['Book_Title'].values

tab1, tab2 = st.tabs(["Recommender System", "Filter by Author"])

with tab1:
    st.header("Recommender System")

    selected_book = st.selectbox(
        "Type or select a book from the dropdown",
        book_list
    )
    author_list = book_author['Book_Author'].values
    if st.button('Show Recommendation books'):
        recommended_book_name,recommended_book_poster,recommended_book_rating,recommended_book_author,recommended_book_similarity = recommendbooks(selected_book)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(recommended_book_poster[0])
            st.write(recommended_book_name[0])
            st.caption(recommended_book_author[0])
            st.text('Rating {}'.format(round(recommended_book_rating[0], 2)))
        with col2:
            st.image(recommended_book_poster[1])
            st.write(recommended_book_name[1])
            st.caption(recommended_book_author[1])
            st.text('Rating {}'.format(round(recommended_book_rating[1], 2)))
            st.caption("similarity about :{} %".format(recommended_book_similarity[1]))
        with col3:
            st.image(recommended_book_poster[2])
            st.write(recommended_book_name[2])
            st.caption(recommended_book_author[2])
            st.text('Rating {}'.format(round(recommended_book_rating[2], 2)))
            st.caption("similarity about :{} %".format(recommended_book_similarity[2]))
        with col4:
            st.image(recommended_book_poster[3])
            st.write(recommended_book_name[3])
            st.caption(recommended_book_author[3])
            st.text('Rating {}'.format(round(recommended_book_rating[3], 2)))
            st.caption("similarity about :{} %".format(recommended_book_similarity[3]))
with tab2:
    st.header("Filter")
    selected_author = st.selectbox("Filter by Author",author_list)
    if st.button('filtering'):
        filter_book_name, filter_book_poster, filter_book_rating, filter_book_author = filterByAuthor(selected_author)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(filter_book_poster[0])
            st.write(filter_book_name[0])
            st.caption(filter_book_author[0])
            st.caption('Rating {}'.format(round(filter_book_rating[0], 2)))

            st.image(filter_book_poster[4])
            st.write(filter_book_name[4])
            st.caption(filter_book_author[4])
            st.caption('Rating {}'.format(round(filter_book_rating[4], 2)))
        with col2:
            st.image(filter_book_poster[1])
            st.write(filter_book_name[1])
            st.caption(filter_book_author[1])
            st.caption('Rating {}'.format(round(filter_book_rating[1], 2)))

            st.image(filter_book_poster[5])
            st.write(filter_book_name[5])
            st.caption(filter_book_author[5])
            st.caption('Rating {}'.format(round(filter_book_rating[5], 2)))
        with col3:
            st.image(filter_book_poster[2])
            st.write(filter_book_name[2])
            st.caption(filter_book_author[2])
            st.caption('Rating {}'.format(round(filter_book_rating[2], 2)))

            st.image(filter_book_poster[6])
            st.write(filter_book_name[6])
            st.caption(filter_book_author[6])
            st.caption('Rating {}'.format(round(filter_book_rating[6], 2)))
        with col4:
            st.image(filter_book_poster[3])
            st.write(filter_book_name[3])
            st.caption(filter_book_author[3])
            st.caption('Rating {}'.format(round(filter_book_rating[3], 2)))

            st.image(filter_book_poster[7])
            st.write(filter_book_name[7])
            st.caption(filter_book_author[7])
            st.caption('Rating {}'.format(round(filter_book_rating[7], 2)))

