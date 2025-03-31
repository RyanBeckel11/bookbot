def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()



def main():
	from stats import character_count
	from stats import num_words
	filepath = "/home/ryanb/workspacebootdev/bookbotproject/bookbot/books/frankenstein.txt"
	book_text = get_book_text(filepath)
	word_count = num_words(book_text)
	word_count_message = f"{word_count} words found in the document"
	count_of_characters = character_count(book_text)
	print(word_count_message)
	print(count_of_characters)
	return (book_text)





main()
