from flask import Flask
from flask import jsonify
app = Flask(__name__)

words = {}

@app.route("/topics/")
def topics():
    return jsonify({
        "words": words
    })

if __name__ == "__main__":
    app.run(debug=True)