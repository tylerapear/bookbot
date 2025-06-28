from stats import get_alpha_character_counts_sorted, get_word_count

def get_book_text(book):
  with open(book) as f:
    return f.read()

def get_word_count(text):
  text_array = text.split()
  return len(text_array)

def main():
  book = get_book_text('./books/frankenstein.txt')
  data_list = get_alpha_character_counts_sorted(book)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {get_word_count(book)} total words")
  print("--------- Character Count -------")

  for item in data_list:
    print(f"{item["name"]}: {item["num"]}")

  print("============= END ===============")

main()