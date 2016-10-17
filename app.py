from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello Internet!"})

@app.route("/bye/")
def bye():
    return "Bye folks"

if __name__ == "__main__":
    app.run(debug=True)