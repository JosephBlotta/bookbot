import sys

from stats import char_num_count, get_num_words, sort_dic


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        num_words = get_num_words(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        dic_words = sort_dic(char_num_count(book))
        for char in dic_words:
            print(f"{char['char']}: {char['num']}")
        print("============= END ===============")
main()
