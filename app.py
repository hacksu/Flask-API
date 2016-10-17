from flask import Flask
from flask import jsonify
app = Flask(__name__)

topics = {}

@app.route("/topics/")
def get_topics():
    return jsonify({
        "topics": topics
    })

@app.route("/topics/<topic>/")
def suggest(topic):
    if topic in topics:
        topics[topic] += 1
    else:
        topics[topic] = 1
    return jsonify({
        "topics": topics
    })

if __name__ == "__main__":
    app.run(debug=True)