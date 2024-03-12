from flask import Flask, render_template, jsonify, send_from_directory, request
from PIL import Image
import json
import os

app = Flask(__name__, static_folder='dataset')

# Load the JSON file
with open('mapping.json') as json_file:
    mapping = json.load(json_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_images/<input_text>')
def get_images(input_text):
    input_text_lower = input_text.lower()  # Convert input to lowercase
    images = []

    # Split the input text into words
    input_words = input_text_lower.split()

    # Check for specific words
    for word in input_words:
        specific_word_filename = mapping.get(word)
        if specific_word_filename:
            images.append({'char': word, 'filename': specific_word_filename})
        else:
            # Retrieve characters and filenames for each character in the lowercase word
            for char in word:
                filename = mapping.get(char)
                if filename:
                    images.append({'char': char, 'filename': filename})

    return jsonify(images)


if __name__ == '__main__':
    app.run(debug=True)
