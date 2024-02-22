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
    # print("doc:", doc, type(doc))
    # Extract keywords (non-stop words and nouns)
    for token in doc:
        if not token.is_stop:
            print(token, token.pos_)
    # print(doc.ents)
    tech_terms = [ent.text for ent in doc.ents if ent.label_ in ["TECHNICAL_TERM", "ORG"]]
    # print("tech_terms:", tech_terms)
    tech_terms = list(set(tech_terms))
    keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    keywords = list(set(keywords))
    print("tech_terms:", tech_terms)
    print("keywords:", keywords)
    for tt in tech_terms:
        for kw in keywords:
            if kw in tt:
                keywords.remove(kw)
        keywords.append(tt)
    keywords = removeRepetitions(keywords)
    return keywords

# print("Title: ")
# title = input()
# print("Description: ")
# description = input()
# title = "Detecting Multiple Reminders from Text Summarization using NLP Techniques"
# description = "The process of automatic reminder generation from conversations typically involves analyzing the text of the conversation to identify key phrases, date, and time. It is a feature that uses Natural Language Processing (NLP) and Machine Learning (ML) to extract information from speech. This information can then be used to automatically create reminders for important tasks or events. Elderly individuals often have difficulty remembering taking medication at specific times. An existing system called Reminder Rosie is designed to solve the very real daily challenges of memory loss. It is a personalized voice-controlled reminder system that elders can use. It reminds our medications, appointments, and every-day tasks. Another platform called Hugging Face which is an NLP platform offers a conversational AI system called \"Reminder Bot.\" This bot allows users to set reminders by simply messaging it with natural language commands. Common drawback for both these systems is the reminders are to be typed manually, which is a tedious process. Our proposed solution is to generate remainders automatically from real-time conversations as they happen and set them as remainders. For this, recorded conversation is converted into text, and then text is summarized with the help of special keywords dataset. These are then added to the Google calendar as remainders. To achieve this, Speech to Text conversion, NLP techniques are used for text summarization. By automatically generating reminders from conversations, users can save time and increase productivity by reducing the need for manual entry of reminders."
# title = "Cognitive Radios for communication during Carrington Event"
# description = "During calamities like Carrington Event, all forms of communication are disrupted and telephones and radios will no longer work. Cognitive Radios can be an effective alternative to be used in such situations for worldwide communication without the effect of geomagnetic storms and solar flares."
# print("\nKEYWORDS\n", extract_keywords(title, description))