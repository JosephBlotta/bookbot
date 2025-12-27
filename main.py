from stats import get_num_words


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
main()
