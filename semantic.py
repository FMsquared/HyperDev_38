import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

""" Notes 

"cat, monkey & banana" similarity:
Expected less similarity between cat and banana than 22.3% 

"""

# Ran my own example of the above 
word1 = nlp("Napoleon")
word2 = nlp("Nelson")
word3 = nlp("Trafalgar")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Ran my example with the simpler language model 
nlp = spacy.load('en_core_web_sm')

word1 = nlp("Napoleon")
word2 = nlp("Nelson")
word3 = nlp("Trafalgar")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

""" Notes 

"sm" versus "md" language models:
The similarity percentages are very much higher as a whole and less contrasting between the individual combinations 

"""