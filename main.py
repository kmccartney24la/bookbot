def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_char_count
import sys

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    print(get_char_count(text))
    print("============= END ===============")
main()
