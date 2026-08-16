# 🎬 Netflix Movie Recommendation System

A content-based movie recommendation system built with Python, Scikit-learn, CountVectorizer, Cosine Similarity, and Streamlit. The system recommends movies based on the similarity of their metadata and content features.

## 🚀 Live Demo

[Open the Live Demo](https://netflix-movie-recommendation-system-8nwfj4aejsbykwqowvi2pq.streamlit.app/)

## 📌 Project Overview

This project uses a content-based filtering approach to recommend movies similar to a movie selected by the user.

The recommendation system processes movie metadata such as:

- Movie title
- Overview
- Genres
- Keywords
- Cast
- Crew information

These features are combined to create a unified representation of each movie. CountVectorizer is used to convert the text-based features into numerical vectors, and Cosine Similarity is used to calculate similarity between movies.

The resulting similarity matrix is used to generate movie recommendations through an interactive Streamlit application.

## ✨ Features

- Select a movie from the available movie dataset.
- Generate movie recommendations based on content similarity.
- Uses multiple movie metadata fields for recommendation.
- Interactive web interface built with Streamlit.
- Precomputed movie and similarity data for faster recommendations.

## 🧠 Recommendation Approach

The system follows these steps:

1. Load the movie metadata and preprocessed data.
2. Combine relevant movie features into a single `tags` representation.
3. Convert text features into numerical vectors using `CountVectorizer`.
4. Calculate similarity between movies using Cosine Similarity.
5. Retrieve the most similar movies for the selected title.
6. Display the recommendations through the Streamlit interface.

## 📊 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

The dataset contains two primary files:

### `tmdb_5000_movies.csv`

Contains movie information such as:

- Title
- Overview
- Genres
- Keywords
- Release information
- Ratings
- Popularity
- Production information

### `tmdb_5000_credits.csv`

Contains:

- Movie ID
- Movie title
- Cast
- Crew

The recommendation system primarily uses:

`title + overview + genres + keywords + cast + crew`

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- Streamlit
- Pickle

## 📁 Project Structure

```text
Netflix-Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gupta-krishna13/Netflix-Movie-Recommendation-System.git
```
Navigate to the project directory:

```bash
cd Netflix-Movie-Recommendation-System
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```


## ▶️ Run Locally
Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

## 🔗 Project Links
Live Demo: https://netflix-movie-recommendation-system-8nwfj4aejsbykwqowvi2pq.streamlit.app/
GitHub Repository: https://github.com/gupta-krishna13/Netflix-Movie-Recommendation-System

## 👨‍💻 Author
Krishna Gupta