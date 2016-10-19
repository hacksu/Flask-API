from flask import Flask
from flask import jsonify
from peewee import *

db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db

class Topic(BaseModel):
    name = CharField()
    count = IntegerField()

db.connect()
db.create_tables([Topic], safe=True)


app = Flask(__name__)


@app.route("/topics/")
def get_topics():
    topics = Topic.select()
    result = {}
    for topic in topics:
        result[topic.name] = topic.count;
    return jsonify({"topics": result})

@app.route("/topics/<topic>")
def suggest(topic):
    try:
        existing_topic = Topic.get(Topic.name==topic)
        existing_topic.count += 1
        existing_topic.save()
    except(DoesNotExist):
        new_topic = Topic(name=topic, count=1)
        new_topic.save()
    return ""


app.run(debug=True)
