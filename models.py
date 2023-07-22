from mongoengine import Document, StringField, ReferenceField

class Movie(Document):
    title = StringField(required=True, max_length=200)
    description = StringField()
    poster = StringField()
    language = StringField()
    # Add any other fields you want for movies

class Show(Document):
    title = StringField(required=True, max_length=200)
    description = StringField()
    # Add any other fields you want for shows
    movie = ReferenceField(Movie)
