def num_words(book_text):
        words = book_text.split()
        word_count = len(words)
        return word_count

def character_count(book_text):
	dict_characters = {}
	lower_text = book_text.lower()
	for character in lower_text:
		if character in dict_characters:
			dict_characters[character] += 1
		else:
			dict_characters[character] = 1
	return dict_characters

def sort_on(dict):
	return dict["count"]

def organized_list(book_text):
	dict_characters = character_count(book_text)
	character_list = []
	for char, count in dict_characters.items():
		character_list.append({"char": char, "count": count})
	character_list.sort(reverse=True, key=sort_on)
	return character_list
