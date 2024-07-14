# import uuid
# #uuid is generate unique ids
# from flask_smorest import Api
# from flask import Flask, abort, request, jsonify
# from db import Authors, Books

# app = Flask(__name__)


# @app.get("/Authors")
# def get_Authors():
#     return {"My Authors": list(Authors.values())}

# @app.get("/Books")
# def get_all_books():
#     return {"books": list(Books.values())}

# @app.get("/authors/<string:authors_name>")
# def get_authors(authors_name):

#     try:
#         return Authors[authors_name]
#     except KeyError:
#         return {"message": "book not found"}, 404
from flask import Flask, request, jsonify
 
 
app = Flask(__name__)
 
authors = []
books = []
 
# Helper function to get the next ID
def get_next_id(data):
    if not data:
        return 1
    max_id = max(item['id'] for item in data)
    return max_id + 1
 
# Author Endpoints
 
@app.route('/authors', methods=['POST'])
def create_author():
    new_author = request.json
    new_author['id'] = get_next_id(authors)
    authors.append(new_author)
    return jsonify(new_author), 201
 
@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(authors)
 
@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author is None:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify(author)
 
@app.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author is None:
        return jsonify({'error': 'Author not found'}), 404
    data = request.json
    author.update(data)
    return jsonify(author)
 
@app.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    global authors
    authors = [a for a in authors if a['id'] != author_id]
    return '', 204
 
# Book Endpoints
 
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    new_book['id'] = get_next_id(books)
    books.append(new_book)
    return jsonify(new_book), 201
 
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)
 
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)
 
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    data = request.json
    book.update(data)
    return jsonify(book)
 
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return '', 204
 
if __name__ == '__main__':
    app.run(debug=True)