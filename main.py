from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

search_books = pd.read_csv('books.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=["POST", "GET"])
def search():

    if request.method == 'POST':
        book_type = request.form['Type']
        genre = request.form['Genre']

        filtered_books = search_books[(search_books['Type'] == book_type) & (search_books['Genre'] == genre)]
        
        return render_template('result.html', books=filtered_books)
    else:
        return ('No results found')

if __name__ == '__main__':
    app.run(debug=True)

