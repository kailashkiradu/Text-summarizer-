# Text Summarizer

This project is a web application that summarizes text using natural language processing (NLP). It uses the spaCy library to process and summarize text inputted by the user.

## Features

- Input any text to be summarized.
- Displays the original and summarized text side by side.
- Shows the word count for both the original and summarized text.
- Responsive and user-friendly interface with animations.

## Requirements

- Python 3.x
- Flask
- spaCy
- jQuery

## Project structure

text-summarizer/
├── app.py
├── TextSummarizer.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── requirements.txt
├── README.md

## Files

app.py
This is the main Flask application file. It handles the web requests and integrates with the TextSummarizer.py to generate summaries.

TextSummarizer.py
This file contains the summarizer function that processes the input text and returns the summarized text along with word counts.

index.html
This is the main HTML file for the web interface. It includes the form for inputting text and displays the original and summarized text.

styles.css
This file contains the CSS styles for the web interface, making it visually appealing and responsive.
