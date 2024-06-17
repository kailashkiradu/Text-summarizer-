import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    # Convert stop words to list
    stopwords = list(STOP_WORDS)

    # Load the small English model from spaCy
    nlp = spacy.load('en_core_web_sm')

    # Process the text using spaCy pipeline
    doc = nlp(rawdocs)

    # Convert the text to tokens
    tokens = [token.text for token in doc]

    # Create a frequency dictionary for words
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # Find the maximum frequency
    max_freq = max(word_freq.values())

    # Normalize the word frequencies
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq

    # Tokenize the sentences
    sent_tokens = [sent for sent in doc.sents]

    # Score the sentences based on word frequencies
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # Select the top 30% of sentences with the highest scores
    select_len = int(len(sent_tokens) * 0.3)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)

    # Join the selected sentences to form the final summary
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))
