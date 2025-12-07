from stats import count_words
from stats import count_chars
from stats import print_results
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books {path}")
        count_words(file_contents)
        count_chars(file_contents)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(sys.argv[1])


    

main()
    