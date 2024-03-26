def main():
  readBook("books/frankenstein.txt")

def readBook(path):
  with open(path) as f:
    file_contents = f.read()
    file_contents_list = file_contents.split()
    word_count = len(file_contents_list)
    character_count = {}

    for word in file_contents_list:
      for char in word:
        lower_char = char.lower()
        if lower_char in character_count:
          character_count[lower_char] += 1
        else:
          character_count[lower_char] = 1

    getReport(path, character_count, word_count)

def getReport(path, chars, word_count):
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document \n")
  letters = 'abcdefghijklmnopqrstuvwxyz'
  for char in chars:
    if char in letters:
      print(f"The '{char}' character was found {chars[char]} times")

main()