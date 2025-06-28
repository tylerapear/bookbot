def get_book_text(book):
  with open(book) as f:
    return f.read()

def count_words(text):
  text_array = text.split()
  return len(text_array)

def main():
  book = get_book_text('./books/frankenstein.txt')
  num_words = count_words(book)
  print(f"{num_words} words found in the document")

main()