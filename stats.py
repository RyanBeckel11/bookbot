def num_words(book_text):
        words = book_text.split()
        word_count = len(words)
        return word_count

def character_count(book_text):
	dict_characters = {}
	lower_text = book_text.lower()
	characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", ",", "?", "!"]
	for character in characters:
		dict_characters[character] = lower_text.count(character)
	return dict_characters

