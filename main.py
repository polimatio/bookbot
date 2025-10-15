import sys
from stats import get_num_words, get_char_count, get_sorted_char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"============ BOOKBOT ============")
    path_to_book = sys.argv[1]
    print(f"Analyzing book found at {path_to_book}...")
    book_text = get_book_text(path_to_book)
    print(f"----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    char_count_dict = get_char_count(book_text)
    sorted_char_count_list = get_sorted_char_count(char_count_dict)
    for char_count_dict in sorted_char_count_list:
        if char_count_dict["char"].isalpha():
            print(f"{char_count_dict["char"]}: {char_count_dict["num"]}")
    print(f"============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as book:
        return book.read()


main()