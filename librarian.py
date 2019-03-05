import re

with open('Perks.txt') as infile:
    text = infile.read()



def get_sentences(text):
	paragraphs = text.split('\n')
	print(len(paragraphs))
	all_sentences = []

	for p in paragraphs:
		sentences = p.split('. ')
		all_sentences += sentences

	return all_sentences


# returns the sentences from a list of sentencess that SEEM like good sentences
#	current filters: must be uppercase
def filter_sentences(sents):
	return [s for s in sents if len(s) > 0 and s[0] == s[0].upper()]

def return_dialog(text):
	paragraphs = text.split('\n')
	dialog_pieces = []	
	
	for paragraph in paragraphs:
		dialog = " ".join(re.findall('"([^"]*)"', paragraph))
		dialog_pieces 


	# def inside_quotes(text):
    # paragraphs = text.split('\n')
    # snowball = ''
    # for p in paragraphs:
    #     in_quotes = " ".join(re.findall('"([^"]*)"', p))
    #     snowball += "\n " + in_quotes
    # return snowball


sents = get_sentences(text)
filtered = filter_sentences(sents)


print(len(sents))
print(len(filtered))

print(filtered[200:300])