# Automatic Trivia Fact Extraction from Wikipedia

### DATASET (Cached Wikipedia Data)
**[LINK To Data ](https://drive.google.com/open?id=0B0JsA9YchOf7SHdlRFBGXzZJY0k)** (one need to be in tamu.edu domain to open it)


### Introduction 
Searching is very important part of present internet era. Most of the search engines try to give you exact and only information you ask through the query. Providing additional interesting facts along with required information makes user search more exploratory and help in increasing the user engagement. The latest search engines have started giving additional information to the user like www.yippy.com and others.


### Data Scrapping 
* **[Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot)** has been used to extract wikipedia data for each searched entity. 
    
### Execution Instructions (to run locally on the machine):

- Download and extract the Google News Word2Vec model into the root folder:
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit 
  This is for the case if the entity is not already searched or cached.

- Install the following Python packages:

    $ pip install gensim

    $ pip install pywikibot
    
    $pip install wikipedia
    
    $ pip install flask
    
    Download nltk corpora, by opening interactive python 
    
    >>> ntlk.download()
    
-  For running the app there are two options:
   
You can either run it from terminal, just type the following command: $ python batchRun.py The above command will automatically start running online for the entities in the topEntityList.txt and generate the output in the outputCache folder for each entity

Alternativly you can run the web app for already cached entities from the data link given above. Download the outputCache folder and run the following command $ python app.py Open the web on localhost at given port, and then just type any entity from the toEntityList.txt and get ranked trivia facts. You can also play Triviathon- Game on this website. 


### Technology stack used
Backend: Backend is powered by python. All the algorithms are written in python.
Full Stack Framework: It is Flask powered framework with python, css, html and javascript. (http://flask.pocoo.org/)

