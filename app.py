from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

#Load data
popular_df = pickle.load(open('Model/popular.pkl','rb'))
pt = pickle.load(open('Model/pt.pkl','rb'))
books = pickle.load(open('Model/books.pkl','rb'))
similarity_scores = pickle.load(open('Model/similarity_scores.pkl','rb'))

#Recommendation Logic
def recommend(book_name):

    try:
        book_name = book_name.strip()

        # Partial matching
        matches = []

        for title in pt.index:
            if book_name.lower() in title.lower():
                matches.append(title)

        if len(matches) == 0:
            return [],None

        selected_book=matches[0]

        index=np.where(pt.index==selected_book)[0][0]

        similar_items=sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:7]

        data = []

        for i in similar_items:

            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            temp_df = temp_df.drop_duplicates('Book-Title')

            item = [
                temp_df['Book-Title'].values[0],
                temp_df['Book-Author'].values[0],
                temp_df['Image-URL-M'].values[0],
                round(i[1] * 100, 2)
            ]

            data.append(item)

        return data, selected_book

    except Exception as e:
        print("ERROR:", e)
        return [], None


#Home Page
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        rating=list(popular_df['avg_rating'].values)
    )


#Recommendation Page
@app.route('/recommend', methods=['GET', 'POST'])
def recommend_page():

    if request.method == 'POST':

        user_input = request.form.get('user_input')

        data, selected_book = recommend(user_input)

        return render_template(
            'recommend.html',
            data=data,
            searched_book=user_input,
            matched_book=selected_book
        )

    return render_template(
        'recommend.html',
        data=None,
        searched_book=None,
        matched_book=None
    )


#Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Run App
if __name__ == '__main__':
    app.run(debug=True)