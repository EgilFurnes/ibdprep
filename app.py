
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Hardcoded questions
questions = [
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Capital of France?", "choices": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Largest planet?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "What is the square root of 16?", "choices": ["2", "4", "8", "16"], "answer": "4"},
    {"question": "Who wrote 'Hamlet'?", "choices": ["Shakespeare", "Dickens", "Hemingway", "Poe"], "answer": "Shakespeare"}
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/question/<int:id>')
def get_question(id):
    question = questions[id % len(questions)]  # Endless loop
    return jsonify(question)

if __name__ == "__main__":
    app.run(debug=True)
