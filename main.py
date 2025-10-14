from stats import get_num_words, get_char_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    char_count = get_char_count(book_text)
    print(f"Character counts: {char_count}")


def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as book:
        return book.read()


main()