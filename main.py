import stats
import sys


book_path = None


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    book_text = get_book_text(book_path)
    num_words = stats.get_num_words(book_text)
    character_counts = stats.get_unique_characters(book_text)
    unique_characters = stats.get_sorted_counts(character_counts)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in unique_characters:
        if item["letter"].isalpha():
            print(f"{item['letter']}: {item['count']}")
    print('============ END ============')


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>)")
    sys.exit(1)
book_path = sys.argv[1]


main()
