import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Sample text
# text = "During calamities like Carrington Event, all forms of communication are disrupted and telephones and radios will no longer work. Cognitive Radios can be an effective alternative to be used in such situations for worldwide communication without the effect of geomagnetic storms and solar flares."
def extract_keywords(title, description):    
    # title = "Detecting Multiple Reminders from Text Summarization using NLP Techniques"
    # description = "The process of automatic reminder generation from conversations typically involves analyzing the text of the conversation to identify key phrases, date, and time. It is a feature that uses Natural Language Processing (NLP) and Machine Learning (ML) to extract information from speech. This information can then be used to automatically create reminders for important tasks or events. Elderly individuals often have difficulty remembering taking medication at specific times. Our proposed solution is to generate remainders automatically from real-time conversations as they happen and set them as remainders. For this, recorded conversation is converted into text, and then text is summarized with the help of special keywords dataset. These are then added to the Google calendar as remainders. To achieve this, Speech to Text conversion, NLP techniques are used for text summarization. By automatically generating reminders from conversations, users can save time and increase productivity by reducing the need for manual entry of reminders."
    combined_text = f"{title}. {description}"
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(combined_text)
    words = [word for sent in sentences for word in word_tokenize(sent.lower()) if word.isalnum()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Create a graph
    G = nx.Graph()

    # Build the graph
    for i, word in enumerate(words):
        for j in range(i + 1, len(words)):
            if i != j:
                G.add_edge(word, words[j])

    # Calculate TextRank scores
    scores = nx.pagerank(G)

    # Rank keywords based on scores
    top_keywords = sorted(scores, key=scores.get, reverse=True)[:5]

    return top_keywords
