from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Load questions from JSON file
with open('questions.json') as f:
    questions = json.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/question/<int:id>')
def get_question(id):
    question = questions[id % len(questions)]  # Endless loop
    return jsonify(question)

if __name__ == "__main__":
    app.run(debug=True)
