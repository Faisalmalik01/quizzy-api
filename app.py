"""
A simple Flask API that serves JS questions from a predefined list of questions.
"""

from flask_cors import CORS 
from flask import Flask, jsonify
from js_questions import questions
import random


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    """
    A simple route to check if the server is running.

    Returns:
        jsonify: A JSON response indicating that the server is running.
    """
    return jsonify({"message": "Server is running!"})


@app.route("/get-question", methods=["GET"])
def get_question():
    """
    A route to get a random question from the 'js_questions' list.

    Returns:
        jsonify: A JSON response containing a random question.
    """
    random_question = random.choice(questions)
    return jsonify(random_question)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=False)
