from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/topics/")
def topics():
    return jsonify({
        "words": {
            "json": 4,
            "jokes": 1,
            "Mobile": 10
        }
    })

if __name__ == "__main__":
    app.run(debug=True)