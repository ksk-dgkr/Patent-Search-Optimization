from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
# import keywords_spacy
import synonyms
import keywords_textrank1

app = Flask(__name__, static_url_path='/static')

# GOOGLE_PATENTS_URL = "https://patents.google.com/patent/"

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/get_query', methods=['POST'])
def get_query():
    title = request.form.get('title')
    description = request.form.get('description')
    # Process the first input using the first Python file
    keywords = keywords_textrank1.extract_keywords(title, description)

    # Process the result from the first file using the second Python file
    synonyms.extract_synonyms(keywords)
    query = synonyms.generate_query()
    return render_template('index.html', query=query)

@app.route('/get_patents', methods=['POST'])
def get_patents():
    query = request.form.get('query')
    if query:
        api_key = 'AIzaSyCDLfKPw-C5LXV0aVpi_xi0ea-uc8T7WuI'
        cx = 'a7ace0a001b444cce'
        # Make a request to Google Custom Search API
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}'
        response = requests.get(url)
        data = response.json()

        # Extract relevant information from the API response
        patents = []
        if 'items' in data:
            for item in data['items']:
                patent = {
                    'title': item.get('title', ''),
                    'link': item.get('link', ''),
                    'snippet': item.get('snippet', ''),
                }
                patents.append(patent)

        return render_template('index.html', patents=patents)

    return render_template('index.html', patents=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
