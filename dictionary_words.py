import sys
import random

def readInFile(word_count, file_name):
  if file_name == False:
    f = open('words.txt','r')
  else:
    f = open(file_name, 'r')
  word_list = f.readlines()
  cleanUpList(word_count, word_list)

def cleanUpList(word_count, word_list):
  new_list = []
  for word in word_list:
    new_word = word.rstrip()
    new_list.append(new_word)
  generateSentance(word_count, new_list)

def generateSentance(word_count, word_list):
  list_length = len(word_list)
  sentence_words = []
  for i in range(5):
    random_word = word_list[random.randint(0, list_length)]
    sentence_words.append(random_word)
  merged_words = " ".join(sentence_words)
  output = merged_words + "."
  print(output)


if __name__ == '__main__':
  word_count = sys.argv[1]
  if(sys.argv[2]):
    readInFile(word_count, sys.argv[2])
  else:
    readInFile(word_count, False)
  