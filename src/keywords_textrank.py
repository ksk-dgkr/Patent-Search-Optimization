import spacy
import pytextrank
# example text
title = "Detecting Multiple Reminders from Text Summarization using NLP Techniques"
description = "The process of automatic reminder generation from conversations typically involves analyzing the text of the conversation to identify key phrases, date, and time. It is a feature that uses Natural Language Processing (NLP) and Machine Learning (ML) to extract information from speech. This information can then be used to automatically create reminders for important tasks or events. Elderly individuals often have difficulty remembering taking medication at specific times. Our proposed solution is to generate reminders automatically from real-time conversations as they happen and set them as remainders. For this, recorded conversation is converted into text, and then text is summarized with the help of special keywords dataset. These are then added to the Google calendar as remainders. To achieve this, Speech to Text conversion, NLP techniques are used for text summarization. By automatically generating reminders from conversations, users can save time and increase productivity by reducing the need for manual entry of reminders."
combined_text = f"{title}. {description}"
# text = "During calamities like Carrington Event, all forms of communication are disrupted and telephones and radios will no longer work. Cognitive Radios can be an effective alternative to be used in such situations for worldwide communication without the effect of geomagnetic storms and solar flares."
# text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
doc = nlp(combined_text)
# examine the top-ranked phrases in the document
# for phrase in doc._.phrases[:10]:
#     print(phrase.text)

# get the top 5 important phrases based on TextRank scores
top_phrases = sorted(doc._.phrases, key=lambda x: x.rank, reverse=True)[:5]

# print the top 5 phrases
for idx, phrase in enumerate(top_phrases, 1):
    print(f"{idx}. {phrase.text} (Rank: {phrase.rank})")


