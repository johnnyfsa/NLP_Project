import spacy

# import model
nlp = spacy.load("pt_core_news_sm")

# text to be verified
source = "Isso é um exemplo de texto que segue um template simples."

# extract relevant information from text
doc = nlp(source)
keywords = ["exemplo", "template simples"]

# verify template conformity
conformity = all(keyword in source for keyword in keywords)


# results

if conformity:
    print('true')
else:
    print('false')
