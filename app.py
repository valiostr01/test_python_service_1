from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/books/<int:id>')
def get_book(id):
    book = {
        "id": id,
        "title": "Flask API Develoment Cookbook",
        "author": "Steven F.Lott",
        "publication_date": "december 2019",
        "publisher": "Packt Publishing",
        "isbn": "9781789959384"
    }
    return  jsonify(book)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)