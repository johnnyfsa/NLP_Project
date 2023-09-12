import spacy

# loading model
nlp = spacy.load("pt_core_news_sm")

# exaple doc
source = "O processamento de linguaguem natural é incrível!"

# process the doc using spacy
doc = nlp(source)

# exibit tokens
for token in doc:
    print(token.text)
