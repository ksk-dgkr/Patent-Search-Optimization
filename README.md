# Patent-Search-Optimization
A search engine application to provide the most relevant patents to an idea description provided as input.
To start using the program, clone the repository.
```
git clone https://github.com/ksk-dgkr/Patent-Search-Optimization.git
```
Install necessary requirements.

### Installations required:
1) Python version 3.10.11 and above
2) Create a virtual environment in your project directory
```
python -m venv myenv
```
3) Activate virtual environment using the command
```
myenv\Scripts\activate
```
Once the environment activates, continue with the installation of other packages mentioned below.

4) Install TextRank for keyword generation
```
pip install pytextrank
```
5) Install SpaCy for various NLP tools
```
python -m spacy download en_core_web_sm
```
6) Install NLTK Package
```
pip install nltk==3.8.1
```
7) Install NetworkX for graph processing
```
pip install networkx
```
8) Install Flask
```
pip install Flask
```
9) Install Requests
```
pip install requests
```

#### Obtain Google Custom Search API Key:
- Go to the Google Developers Console.
- Create a new project or select an existing one.
- Enable the "Custom Search JSON API" for your project.
Create credentials and obtain the API key.

(Refer to the sites mentioned:      
https://developers.google.com/custom-search/v1/introduction  
https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/    
https://console.cloud.google.com/apis/dashboard?authuser=0&project=patent-search-1704376993185)

#### Configure API Key:
- Open the app.py file.
- Replace the API Key placeholder with the ontained Google Custom Search API key.

#### Usage:
Run the Flask application
```
python app.py
```
- The application runs in the web browser at http://localhost:5000.
- Enter the title and description of your idea and submit the form.
- View the retrieved patents related to your input idea.
