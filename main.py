def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()



def main():
	filepath = "/home/ryanb/workspacebootdev/bookbotproject/bookbot/books/frankenstein.txt"
	book_text = get_book_text(filepath)
	word_count = num_words(book_text)
	word_count_message = f"{word_count} words found in the document"
	print(word_count_message)
	return (book_text)




def num_words(book_text):
	words = book_text.split()
	word_count = len(words)
	return word_count

main()
