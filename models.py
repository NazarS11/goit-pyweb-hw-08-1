from datetime import datetime

from mongoengine import EmbeddedDocument, Document, ReferenceField, CASCADE
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)