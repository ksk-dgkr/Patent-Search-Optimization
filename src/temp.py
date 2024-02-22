#all
import tkinter as tk
from tkinter import scrolledtext
import spacy
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import nltk


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

def extract_keywords():
    title = title_entry.get()
    description = description_text.get("1.0", "end-1c")
    
    if not title or not description:
        result_text.delete("1.0", "end")
        result_text.insert(tk.END, "Both title and description are required.")
        return
    
    # Combine title and description for keyword extraction
    combined_text = f"{title}\n{description}"
    
    # Process the text using spaCy
    doc = nlp(combined_text)   
    
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ["TECHNICAL_TERM", "ORG"]]
    tech_terms = list(set(tech_terms))
    keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    keywords = list(set(keywords))

    for tt in tech_terms:
        for kw in keywords:
            if kw in tt:
                keywords.remove(kw)
        keywords.append(tt)
        
    keywords = removeRepetitions(keywords)

    # Display the extracted keywords in the result_text widget
    result_text.delete("1.0", "end")
    result_text.insert(tk.END, "Keywords:\n\n")
    result_text.insert(tk.END, "\n".join(keywords), "\n")
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

        for i in range(3):
            if i < len(synonyms):
                synonyms[i] = synonyms[i].replace("_", " ")

        keywords_and_synonyms[keyword] = synonyms[:3]  # Get the first three synonyms
        result_text.insert(tk.END, f"{keyword}: {', '.join(synonyms[:3])}\n")
        
    with open("search_terms.txt", "w") as file:
        for keyword, synonyms in keywords_and_synonyms.items():
            file.write(f"{keyword},{','.join(synonyms)}\n") 
        file.close()
    # Save keywords and synonyms to a file
    

def generate_query():
    
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
    result_text.delete("1.0", "end")
    result_text.insert(tk.END, "Generated Query Expressions:\n\n")
    result_text.insert(tk.END, "\n".join(final_query))
    
    
# Create the main window
root = tk.Tk()
root.title("Keyword Extraction")

# Create and pack a label for the title
title_label = tk.Label(root, text="Title:")
title_label.pack()

# Create and pack an entry widget for the title
title_entry = tk.Entry(root)
title_entry.pack()

# Create and pack a label for the description
description_label = tk.Label(root, text="Description:")
description_label.pack()

# Create and pack a scrolled text widget for the description
description_text = scrolledtext.ScrolledText(root, height=5, width=40)
description_text.pack()

# Create and pack an "Extract Keywords" button
extract_button = tk.Button(root, text="Extract Keywords", command=extract_keywords)
extract_button.pack()

query_button = tk.Button(root, text="Generate Query", command=generate_query)
query_button.pack()

# Create and pack a label for the result
result_label = tk.Label(root, text="Keywords:")
result_label.pack()

# Create and pack a scrolled text widget for displaying the keywords
result_text = scrolledtext.ScrolledText(root, height=100, width=100)
result_text.pack()

# Start the Tkinter main loop
root.mainloop()















# import tkinter as tk
# from tkinter import scrolledtext
import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")
def removeRepetitions(words):
    words = [word.lower() for word in words]
    words = list(set(words))
    return words
    
def extract_keywords(title, description):
    
    combined_text = f"{title}. {description}"
    # print("combined:", combined_text, type(combined_text))
    
    # Process the text using spaCy
    doc = nlp(combined_text)
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ["TECHNICAL_TERM", "ORG"]]
    tech_terms = list(set(tech_terms))
    keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    keywords = list(set(keywords))

    for tt in tech_terms:
        for kw in keywords:
            if kw in tt:
                keywords.remove(kw)
        keywords.append(tt)
        
    keywords = removeRepetitions(keywords)
    
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ["TECHNICAL_TERM", "ORG"]]
    tech_terms = list(set(tech_terms))
    keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    keywords = list(set(keywords))
    print("tech_terms:", tech_terms)
    print("\nkeywords:", keywords)
    for tt in tech_terms:
        for kw in keywords:
            if kw in tt:
                keywords.remove(kw)
        keywords.append(tt)
    print("\nall keywords:", keywords)
    keywords = [keyword.lower() for keyword in keywords]
    lemmatized_keywords = []
    for keyword in keywords:
        for token in doc:
            if token.text == keyword:
                lemma = token.lemma_
                break
        lemmatized_keywords.append(lemma)
    # lemmatized_keywords = [token.lemma_ for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    print("\nlemmatized_keywords:", lemmatized_keywords)
    # lemmatized_keywords = [keyword.lower() for keyword in lemmatized_keywords]
    unique_keywords = []
    for keyword in lemmatized_keywords:
        if keyword not in unique_keywords:
            unique_keywords.append(keyword)
    # unique_keywords = removeRepetitions(keywords)
    print(unique_keywords)
    word_frequency = {word: lemmatized_keywords.count(word) for word in unique_keywords}
    print("\nword_frequency:", word_frequency)

    # keywords = removeRepetitions(keywords)
    # Sort keywords based on importance score
    sorted_keywords = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    print("\nsorted_keywords:", sorted_keywords)
    # Get the top 5 important keywords
    top_keywords = [keyword[0] for keyword in sorted_keywords[:5]]
    
    print("\nTop 5 Keywords:", top_keywords)
    return top_keywords
    # return keywords

    
# print("Title: ")
# title = input()
# print("Description: ")
# description = input()
# title = "Detecting Multiple Reminders from Text Summarization using NLP Techniques"
# description = "The process of automatic reminder generation from conversations typically involves analyzing the text of the conversation to identify key phrases, date, and time. It is a feature that uses Natural Language Processing (NLP) and Machine Learning (ML) to extract information from speech. This information can then be used to automatically create reminders for important tasks or events. Elderly individuals often have difficulty remembering taking medication at specific times. An existing system called Reminder Rosie is designed to solve the very real daily challenges of memory loss. It is a personalized voice-controlled reminder system that elders can use. It reminds our medications, appointments, and every-day tasks. Another platform called Hugging Face which is an NLP platform offers a conversational AI system called \"Reminder Bot.\" This bot allows users to set reminders by simply messaging it with natural language commands. Common drawback for both these systems is the reminders are to be typed manually, which is a tedious process. Our proposed solution is to generate reminders automatically from real-time conversations as they happen and set them as reminders. For this, recorded conversation is converted into text, and then text is summarized with the help of special keywords dataset. These are then added to the Google calendar as reminders. To achieve this, Speech to Text conversion, NLP techniques are used for text summarization. By automatically generating reminders from conversations, users can save time and increase productivity by reducing the need for manual entry of reminders."
# # title = "Cognitive Radios for communication during Carrington Event"
# # description = "During calamities like Carrington Event, all forms of communication are disrupted and telephones and radios will no longer work. Cognitive Radios can be an effective alternative to be used in such situations for worldwide communication without the effect of geomagnetic storms and solar flares."
# print("\nKEYWORDS\n", extract_keywords(title, description))