# BookAI - Book Recommendation System

## About the Project

BookAI is a machine learning-based book recommendation system built using Python and Flask. The goal of this project is to help readers discover new books based on books they already enjoy.

I have always enjoyed reading, and one challenge I noticed was finding similar books after finishing a great one. This project was created to solve that problem by recommending books with similar user rating patterns.

The system uses collaborative filtering and cosine similarity to generate recommendations from a dataset of books and user ratings.

---

## Live Link : # Book Recommendation System

🔗 Live Demo: https://book-recommender-system-j47e.onrender.com

## Features

* View Top 50 Popular Books
* Search books by title
* Partial title matching
* Get similar book recommendations
* Similarity percentage display
* Responsive user interface
* Contact/About page

---

## Dataset

## Dataset

This project uses the 'Book Recommendation Dataset' from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

### Dataset Files
- Books.csv – Information about books (title, author, publisher, year, ISBN)
- Users.csv – User demographic information
- Ratings.csv – User ratings for books

### Dataset Statistics
- ~270,000 books
- ~1 million ratings
- ~278,000 users

The recommendation model is built using collaborative filtering based on user-book interactions.

## How It Works

1. User enters a book title.
2. The system finds the closest matching book in the dataset.
3. A similarity matrix is used to identify books with similar rating patterns.
4. The top recommendations are displayed to the user.

The recommendation engine is based on collaborative filtering and cosine similarity.

---

## Technologies Used

### Backend

* Python
* Flask

### Machine Learning & Data Processing

* Pandas
* NumPy
* Scikit-learn

### Frontend

* HTML
* CSS

### Deployment

* Render

---

## Project Structure

## Project Structure

```text
BookAI-BookRecommenderSystem/
│
├── .venv/
├── Model/
│   ├── books.pkl
│   ├── popular.pkl
│   ├── pt.pkl
│   └── similarity_scores.pkl
│
├── templates/
│   ├── index.html
│   ├── recommend.html
│   └── contact.html
│
├── static/
│   └── style.css
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Folder Description

- **Model/** – Stores trained recommendation model files and serialized data.
- **templates/** – HTML templates used by Flask.
- **static/** – CSS and static assets.
- **app.py** – Runs the Flask web application.
- **main.py** – Data preprocessing and model generation script.
- **requirements.txt** – Python dependencies.
- **README.md** – Project documentation.

## Future Improvements

* User authentication
* Favorite books feature
* Search history
* Database integration
* Hybrid recommendation system
* Book genre filtering
* REST API support

---

## Challenges Faced

One of the main challenges was handling large recommendation data efficiently. To improve performance, the similarity matrix and processed datasets were stored using pickle files so they could be loaded quickly when the application starts.

Another challenge was implementing accurate book matching while allowing users to search using partial book titles.

---

## What I Learned

Through this project, I gained practical experience with:

* Machine Learning recommendation systems
* Collaborative filtering
* Cosine similarity
* Flask web development
* Data preprocessing with Pandas
* Deploying web applications

---

## Author

Shivani Pandey

Computer Science Student

GitHub: https://github.com/shivanipandey24

LinkedIn: https://linkedin.com/in/shivanipandey-cse
