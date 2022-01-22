import random

def randomize_words(submitted_words):
  split_words = submitted_words.split(' ')
  print(split_words)
  random.shuffle(split_words)
  print(split_words)

if __name__ == '__main__':
    submitted_words = input('Give some words')
    randomize_words(submitted_words)