Book Recommendation System
A content-based book recommendation system built with Python and deployed as an interactive web application using Streamlit.
➡️ View Live Demo
Description
This project is a web application that suggests books to users based on their selections. It uses a content-based filtering approach, analyzing book metadata such as title, author, language, and publisher to identify and recommend similar items. The intuitive interface allows users to easily find new books to read.
Features
Interactive UI: A simple and clean user interface built with Streamlit.
Content-Based Filtering: Recommends books by analyzing their textual features.
Large Dataset: Utilizes a dataset of over 11,000 books.
Real-time Recommendations: Instantly generates a list of the top 11 most similar books.
How It Works
The recommendation engine is built on the principles of Natural Language Processing (NLP) and information retrieval:
Data Preprocessing: Book metadata (title, author, language, and publisher) is cleaned and combined into a single text string for each book.
TF-IDF Vectorization: Each book's combined text is converted into a numerical vector using Term Frequency-Inverse Document Frequency (TF-IDF). This technique represents the importance of each word in the text relative to the entire collection of books.
Cosine Similarity: When a user selects a book, the cosine similarity is calculated on-the-fly between the selected book's vector and all other book vectors in the dataset. A higher cosine similarity score indicates a greater resemblance.
Recommendation: The books with the highest similarity scores are then presented to the user as recommendations.
Tech Stack
Python: Core programming language.
Pandas: For data manipulation and processing.
Scikit-learn: For TF-IDF vectorization and cosine similarity calculation.
Streamlit: For building and deploying the interactive web application.
Setup and Local Installation
To run this project on your local machine, follow these steps:
Clone the repository:
git clone https://github.com/pandey-aditya04/book-recommender


Navigate to the project directory:
cd book-recommender


Install the required libraries:
pip install -r requirements.txt


Run the Streamlit app:
streamlit run app.py


