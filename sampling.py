import sys
from random import randint
from histogram import *

def generateRandomWord(word_text, dictionary):
  count = 0
  return_word = ''
  total_words = len(word_text)
  random_number = randint(0,total_words)
  for key in dictionary:
    if count <= random_number:
      value = dictionary[key]
      count += value
      return_word = key
    if count > random_number:
      break
  print(return_word)
  return return_word

if __name__ == '__main__':
  file_name = sys.argv[1]
  word_text = readInFile(file_name)
  dictionary = histogramDict(word_text)
  generateRandomWord(word_text, dictionary)