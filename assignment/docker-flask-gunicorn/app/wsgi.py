from flask import Flask, request
from transformers import pipeline
import json

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Create Flask app instance
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

# Define route for sentiment analysis
@app.route('/sentiment', methods=["GET", "POST"])
def sentiment():
     
    text = request.json['text']
    result = classifier(text)
    return result[0]['label']
 

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)