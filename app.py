from flask import Flask
from flask import jsonify
app = Flask(__name__)

topics = {}

@app.route("/topics/")
def topics():
    return jsonify({
        "topics": topics
    })

if __name__ == "__main__":
    app.run(debug=True)