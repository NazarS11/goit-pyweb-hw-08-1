import json
from models import Author, Quote
from connect import connect

def load_data():
    with open('authors.json', 'r') as file:
        authors_data = json.load(file)
        for data in authors_data:
            author = Author.objects(fullname=data['fullname']).first()
            if not author:
                author = Author(
                    fullname=data['fullname'],
                    born_date=data['born_date'],
                    born_location=data['born_location'],
                    description=data['description']
                )
                author.save()

    with open('quotes.json', 'r') as file:
        quotes_data = json.load(file)
        for data in quotes_data:
            author = Author.objects(fullname=data['author']).first()
            if author:
                quote = Quote(
                    tags=data['tags'],
                    author=author,
                    quote=data['quote']
                )
                quote.save()


if __name__ == '__main__':
    load_data()
