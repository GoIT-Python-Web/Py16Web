from mongoengine import *

connect(
    db="web16",
    host="mongodb+srv://userweb16:*****@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
)


class Task(Document):
    completed = BooleanField(default=False)
    consumer = StringField(max_length=150)
