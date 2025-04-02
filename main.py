import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()



def main():
	from stats import character_count
	from stats import num_words
	from stats import organized_list
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	word_count = num_words(book_text)
	word_count_message = f"{word_count} words found in the document"
	count_of_characters = character_count(book_text)
	organized_list = organized_list(book_text)
	print("============ BOOKBOT ============")
	print("Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for character_dict in organized_list:
		character = character_dict["char"]
		if character.isalpha():
			count = character_dict["count"]
			print(f"{character}: {count}")
	print("============= END ===============")
	return (book_text)





main()
