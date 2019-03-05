import re

def get_sentences(text):
	paragraphs = text.split('\n')
	print(len(paragraphs))
	all_sentences = []

	for p in paragraphs:
		sentences = p.split('. ')
		all_sentences += sentences

	return all_sentences

def clean(text):
	return text.replace('”','"').replace('“','"')


# returns the sentences from a list of sentencess that SEEM like good sentences
#	current filters: must be uppercase
def filter_sentences(sents):
	return [s for s in sents if len(s) > 0 and s[0] == s[0].upper()]

def get_dialog(text):
	paragraphs = text.split('\n')
	lines = []	
	
	for paragraph in paragraphs:
		#print(paragraph)
		new_lines = re.findall('"([^"]*)"', paragraph)
		#print(new_lines)
		lines += new_lines

	return lines

def get_search_terms_list(category_name):
	filepath = 'response_categories/' + category_name + '.txt'
	with open(filepath) as input_file:
		return input_file.readlines()

def any_search_term_in(line, search_terms):



if __name__ == '__main__':
	with open('Perks.txt') as infile:
		text = clean(infile.read())

	sents = get_sentences(text)
	filtered = filter_sentences(sents)

	lines = get_dialog(text)
	print(lines)

	print(len(lines))
	# all lines less than 20 characters long
	short_lines = [line for line in lines if len(list(line)) < 20]

	print(len(short_lines))
	print(short_lines)

	short_questions = [line for line in short_lines if line[-1] == '?']

	print(short_questions)

	search_terms = get_search_terms_list()

	greetings = [line for line in lines if any_search_term_in(line, search_terms)] 

