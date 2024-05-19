from mongoengine import connect, Document, StringField, ListField, ObjectIdField
import sys
from models import Author, Quote
import connect

def find_quotes_by_author_name(author_name):
    # Знаходження автора за ім'ям
    author = Author.objects(fullname=author_name).first()
    if not author:
        return "No author found with the name {}".format(author_name)
    
    # Знаходження цитат цього автора
    quotes = Quote.objects(author=author.id)
    return '\n'.join([q.quote for q in quotes]) if quotes else "No quotes found for author {}".format(author_name)

def find_quotes_by_tag(tag):
    # Знаходження цитат за одним тегом
    quotes = Quote.objects(tags=tag)
    return '\n'.join([q.quote for q in quotes]) if quotes else "No quotes found for tag {}".format(tag)

def find_quotes_by_tags(tags):
    # Знаходження цитат за декількома тегами
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return '\n'.join([q.quote for q in quotes]) if quotes else "No quotes found for tags {}".format(tags)

# Головний цикл програми
def main():
    while True:
        user_input = input("Enter command (name/tag/tags/exit): ")
        if user_input.lower() == 'exit':
            print("Exiting program.")
            break
        
        if ':' not in user_input:
            print("Invalid command format.")
            continue
        
        command, value = user_input.split(':', 1)
        value = value.strip()
        
        if command == 'name':
            result = find_quotes_by_author_name(value)
        elif command == 'tag':
            result = find_quotes_by_tag(value)
        elif command == 'tags':
            result = find_quotes_by_tags(value)
        else:
            print("Invalid command. Try again.")
            continue
        
        print(result)

if __name__ == "__main__":
    main()
