# Importing necessary libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pandas as pd

# Function to summarize text
def summarize(text, per=0.3):
    # Load the spaCy English language model
    nlp = spacy.load('en_core_web_sm')

    # Tokenize the input text
    doc = nlp(text)
    
    # Extract tokens from the document
    tokens = [token.text for token in doc]
    
    # Create a dictionary to store word frequencies
    word_frequencies = {}
    
    # Calculate word frequencies, excluding stop words and punctuation
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    
    # Normalize word frequencies
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
    
    # Tokenize the text into sentences
    sentence_tokens = [sent for sent in doc.sents]
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    
    # Select a portion of sentences based on the given percentage
    select_length = int(len(sentence_tokens) * per)
    
    # Extract the summary sentences using nlargest
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    
    # Extract the text content from the summary sentences
    final_summary = [word.text for word in summary]
    
    # Concatenate the summary sentences to form the final summary
    summary = ''.join(final_summary)
    
    return summary
