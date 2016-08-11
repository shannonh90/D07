# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(wordlist):
	capital_list = []

	for word in wordlist:
		if type(word) is list:
			word = capitalize_nested(word)
		else:
			word = word.capitalize()
		capital_list.append(word)
	return capital_list

	# for word in wordlist:
	# 	if type(word) is list:
	# 		capital_word = str(wordlist).capitalize()
	# 	capital_list.append(capital_word)

	# print capital_list



#################################################################

def main():
	print(capitalize_nested(['shannon', ['cat'], 'hamilton']))
	


if __name__ == '__main__':
    main()