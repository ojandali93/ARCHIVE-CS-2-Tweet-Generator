import sys
from sampling import *

def runTesting():
  return_dict = {}
  for i in range(1000):
    returned_word = generateRandomWord(word_text, dictionary)
    if returned_word in return_dict.keys():
      return_dict[returned_word] += 1 
    else:
      return_dict[returned_word] = 1
  print(return_dict)


if __name__ == '__main__':
  file_name = sys.argv[1]
  word_text = readInFile(file_name)
  dictionary = histogramDict(word_text)
  runTesting()