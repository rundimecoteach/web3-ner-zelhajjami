from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

import textacy.extract

from bs4 import BeautifulSoup
import requests
import re

nlp = en_core_web_sm.load()

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

ny_bb = url_to_string('https://www.biography.com/people/brad-pitt-9441989')

article = nlp(ny_bb)
len(article.ents)

labels = [x.label_ for x in article.ents]
Counter(labels)
pprint([(X, X.ent_iob_, X.ent_type_) for X in article if X.ent_type_=='PERSON'])

sentences = [x for x in article.sents]
#print(sentences[20])

displacy.serve(article, style='ent')
"""
for word in article:
    if word.dep_ in ('father', 'mother'):
        print(''.join(w.text_with_ws for w in word.subtree))
"""


statements = textacy.extract.semistructured_statements(article, "father")
# Print the results
print("Here are the things I know about mother:")

for statement in statements:
    subject, verb, fact = statement
    print(" - Statement: ", statement)
    print(" - Fact: ", fact)


