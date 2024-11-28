from flask import Flask, jsonify, render_template, redirect
import json

app = Flask(__name__)

# Load questions from JSON file
with open('questions.json') as f:
    questions = json.load(f)

@app.route('/')
def home():
    return redirect('/question/0')

@app.route('/question/<int:id>')
def get_question(id):
    question = questions[id % len(questions)]  # Endless loop
    return jsonify(question)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
