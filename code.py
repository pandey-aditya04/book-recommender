import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the saved data and models using Streamlit's caching for performance
@st.cache_data
def load_data():
    """Loads the pre-processed DataFrame and TF-IDF vectors."""
    df = pickle.load(open('df.pkl', 'rb'))
    vectors = pickle.load(open('vectors.pkl', 'rb'))
    return df, vectors

# Load the data once when the app starts
df, vectors = load_data()

def recommend(book_title):
    try:

        book_index = df[df['title'] == book_title].index[0]
        distances = cosine_similarity(vectors[book_index], vectors)
        scores = list(enumerate(distances[0]))
        sorted_scores = sorted(scores, reverse=True, key=lambda x: x[1])
        similar_books_indices = sorted_scores[1:12]
        
        recommended_books = []
        for item in similar_books_indices:
            index = item[0]
            recommended_books.append(df['title'][index])
            
        return recommended_books

    except IndexError:
        return ["Book not found. Please select a book from the list."]

# --- Streamlit Web Interface ---

st.title('📚 Book Recommendation System')
st.write("Select a book from the dropdown menu and click 'Recommend' to get similar book suggestions.")

selected_book_name = st.selectbox(
    'Type or select a book from the dropdown',
    df['title'].values
)

if st.button('Recommend'):
    if selected_book_name:
        recommendations = recommend(selected_book_name)
        st.subheader("Recommended Books:")
        # Display the list of recommended books
        for i, book in enumerate(recommendations, 1):
            st.write(f"{i}. {book}")
    else:
        st.write("Please select a book first.")

