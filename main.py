from stats import get_alpha_character_counts_sorted, get_word_count
import sys

args = sys.argv

def get_book_text(book):
  with open(book) as f:
    return f.read()

def get_word_count(text):
  text_array = text.split()
  return len(text_array)

def main():
  if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book = get_book_text(args[1])
    data_list = get_alpha_character_counts_sorted(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book)} total words")
    print("--------- Character Count -------")

    for item in data_list:
      print(f"{item["name"]}: {item["num"]}")

    print("============= END ===============")

main()