import spacy

nlp = spacy.load('en_core_web_md')

with open('Perks.txt') as f:
    text = f.read()

doc = nlp(text[:20000])

token_strings = [token.text for token in doc]
vectors = [token.vector for token in doc]

# see vector for PERKS
# print(token_strings[1])
# print(vectors[1])

# see similarity between THE and PERKS
# print(doc[0].similarity(doc[1]))

# see similarity between first 30 words in text and THE
for idx, vector in enumerate(doc[:30]):
    print(doc[idx])
    print(doc[0].similarity(doc[idx]))