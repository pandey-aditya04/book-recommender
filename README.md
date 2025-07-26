# 📚 Book Recommendation System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![GitHub license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/pandey-aditya04/book-recommender/blob/main/LICENSE)

A content-based book recommendation system built with Python and deployed as an interactive web application using Streamlit. This app suggests books to users based on their selections, helping them discover their next great read!

<a href="YOUR_LIVE_DEMO_URL_HERE" target="_blank">
  <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App">
</a>

***

## ✨ Features

-   **Interactive UI**: A simple, clean, and intuitive user interface built with Streamlit.
-   **Content-Based Filtering**: Recommends books by analyzing textual features like title, author, language, and publisher.
-   **Large Dataset**: Utilizes a dataset of over 11,000 books to provide a wide range of recommendations.
-   **Real-time Recommendations**: Instantly generates a list of the top 11 most similar books.

***

## 🧠 How It Works

The recommendation engine is built on the principles of Natural Language Processing (NLP) and information retrieval:

1.  **Data Preprocessing**: Book metadata (title, author, language, and publisher) is cleaned and combined into a single text string for each book.

2.  **TF-IDF Vectorization**: Each book's combined text is converted into a numerical vector using **Term Frequency-Inverse Document Frequency (TF-IDF)**. This technique represents the importance of each word relative to the entire collection of books.

3.  **Cosine Similarity**: When a user selects a book, the **cosine similarity** is calculated on-the-fly between the selected book's vector and all other book vectors in the dataset. A higher cosine similarity score indicates a greater resemblance.

4.  **Recommendation**: The books with the highest similarity scores are then presented to the user as recommendations.

***

## 🛠️ Tech Stack

-   **Core Language**: Python
-   **Data Manipulation**: Pandas
-   **Machine Learning**: Scikit-learn
-   **Web Framework**: Streamlit

***

## 🚀 Setup and Local Installation

To run this project on your local machine, follow these steps:

### **1. Clone the Repository**

```bash
git clone [https://github.com/pandey-aditya04/book-recommender](https://github.com/pandey-aditya04/book-recommender)
```

### **2. Navigate to the Project Directory**

```bash
cd book-recommender
```

### **3. Install the Required Libraries**

```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit App**

```bash
streamlit run app.py
```

Open your web browser and navigate to `http://localhost:8501` to see the app in action!

***

## 📂 Project Structure

```
book-recommender/
│
├── app.py             # Main Streamlit application file
├── requirements.txt   # List of project dependencies
├── dataset.csv        # The book dataset used for recommendations
└── README.md          # This file
```
