# Step 1: scrape text from url:
We start by creating the corpus, our corpus is texts from the net, we used URL of celebrity's biography, 
links we used: </br>
    - https://www.sahistory.org.za/article/nelson-mandela-family-tree </br>
    - https://www.biography.com/people/ellen-degeneres-9542420 </br>
    - https://www.biography.com/people/brad-pitt-9441989 </br>
since these texts correspond to the expectations of our ontology (relationship between family member).
our idea is to put a list of links that are stored in a file to properly feed our corpus
# Step 2: Using Spacy:
## defining the language:
Since out texts are in english we chose to use the language model en_core_web_sm (using English texts give more accuracy)

## cleaning the output
We are interested onley in type "PERSON" so we applied a filter on the output to extract onley Persons from the text

## extracting facts
To know the relation between Persons we had to extract facts about them, we basically take the sentence after the "relation", for example "
