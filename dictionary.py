letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.lower().split()

def hash_dictionary(letter):
	dictionary = {}

	temp = open('Dictionary\\{}.csv'.format(letter), 'r').readlines()

	for line in temp:
		temp_list = line.strip().lower().split('---')

		if '---(' in line and ')---' in line and len(temp_list) == 3:
			if  temp_list[0] not in dictionary:
				dictionary[temp_list[0]] = [temp_list[1] + ": " + temp_list[2]]

			elif '---(' in line and ')---' in line and len(dictionary[temp_list[0]]) < 3:
				dictionary[temp_list[0]].append(temp_list[1] + ": " + temp_list[2])

	return dictionary

class l_dictionary:
	def __init__(self, l_dict):
		self.l_dict = l_dict

	def return_def(self, word):
		return self.l_dict[word.lower().strip()]

	def return_dict(self):
		return(self.l_dict)

dictionary = {}
for letter in letters:
	dictionary[letter] = l_dictionary(l_dict=hash_dictionary(letter))

def get_definition(word):
	try:
		return list(dictionary[word[0]].return_def(word))
	except KeyError:
		return ['No such word exists in our dictionary.']

def random_word():
	import random
	rd = dictionary[letters[random.randint(1,26)]].return_dict()
	return random.choice(list(rd.items()))
