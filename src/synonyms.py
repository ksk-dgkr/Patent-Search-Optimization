#all
# import tkinter as tk
# from tkinter import scrolledtext
import spacy
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords



# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Download NLTK's stopwords and WordNet data
nltk.download('stopwords')
nltk.download('wordnet')

def removeRepetitions(words):
    words = [word.lower() for word in words]
    words = list(set(words))
    return words

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def extract_synonyms(keywords):
    keywords_and_synonyms = {}
    for keyword in keywords:
        synonyms = get_synonyms(keyword)
        synonyms = list(set(synonyms))
        if keyword in synonyms: 
            synonyms.remove(keyword)
        if keyword.lower() in synonyms:
            synonyms.remove(keyword.lower())
        if keyword.upper() in synonyms:
            synonyms.remove(keyword.upper())
        synonyms_str = ", ".join(synonyms[:3])  # Get the first three synonyms
        print(f"{keyword}: {synonyms_str}\n")
        for i in range(3):
            if i < len(synonyms):
                synonyms[i] = synonyms[i].replace("_", " ")
        keywords_and_synonyms[keyword] = synonyms[:3]
    
    print(keywords_and_synonyms)
    
    with open("search_terms.txt", "w") as file:
        for keyword, synonyms in keywords_and_synonyms.items():
            if synonyms == []:
                file.write(f"{keyword}\n")
            else:
                file.write(f"{keyword},{','.join(synonyms)}\n") 
        file.close()

def generate_query():
    # with open("search_terms.txt", "r") as file:
    #     search_terms = file.read().splitlines()
    
    # # Generate Boolean query expression using extracted keywords and synonyms
    # query_expressions = []
    # for keyword_and_synonyms in keywords_and_synonyms:
    #     keyword, *synonyms = keyword_and_synonyms.split(': ')
    #     synonyms_expression = f" AND ".join(synonyms)
    #     query_expression = f"({keyword} OR ({synonyms_expression}))"
    #     query_expressions.append(query_expression)
    # # Read the contents of the .txt file
    with open('search_terms.txt', 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store individual line queries
    line_queries = []
    # Process each line in the file
    for line in lines:
        # Split the line into individual strings using a comma as the separator
        strings = line.strip().split(',')
        # Create an ORed query for the strings in the line
        line_query = ' OR '.join(strings)
        # Append the ORed query to the list of line queries
        line_queries.append(f'({line_query})')

    # Join all line queries with AND to create the final query
    final_query = ' AND '.join(line_queries)
    # Print the final query
    print()
    print(final_query)
    return final_query
    # return '(machine learning)'
    # print(query_expressions)

# keywords = ['effect', 'storms', 'flares', 'carrington event', 'communication', 'alternative', 'telephones', 'situations', 'forms', 'calamities', 'radios']
# keywords = ['rosie', 'events', 'commands', 'natural', 'solution', 'speech', 'voice', 'date', 'platform', 'techniques', 'productivity', 'system', 'time', 'text', 'challenges', 'nlp', 'process', 'generation', 'remainders', 'phrases', 'drawback', 'ai', 'reminders', 'conversation', 'individuals', 'multiple', 'information', 'tasks', 'medication', 'day', 'reminder', 'google', 'need', 'processing', 'hugging face', 'difficulty', 'summarization', 'medications', 'help', 'bot', 'systems', 'memory', 'loss', 'conversion', 'entry', 'machine learning', 'ml', 'appointments', 'language', 'feature', 'conversations', 'elders', 'text summarization', 'times', 'calendar', 'keywords', 'users']
# keywords = ['ml', 'ML'] 
# extract_synonyms(keywords)
# generate_query()