import sys
from stats import get_word_count, get_char_count


def get_book_text(filepath: str) -> str:
    """
    Reads filepath parameter.
    Expects filepath to be a path to the book to be read.
    Returns the contents of the book.
    """
    with open(filepath) as f:
        return f.read()


def generate_report(filepath: str, word_count: int, char_count):
    """Displays report to stdout with all the stats"""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


def main():
    """Main function to run entire app"""

    # Check if a path argument for the input book is passed
    if len(sys.argv) != 2:
        # Prints out usage message and returns status code 1
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get all stats
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    word_count = get_word_count(content)
    char_count = get_char_count(content)

    generate_report(book_path, word_count, char_count)


if __name__ == "__main__":
    main()
