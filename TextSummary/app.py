from flask import Flask, render_template, request, jsonify
from TextSummarizer import summarizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        raw_text = request.form['text']
        summary, doc, original_length, summary_length = summarizer(raw_text)
        return jsonify({
            'summary': summary,
            'original_word_count': original_length,
            'summary_word_count': summary_length
        })
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
