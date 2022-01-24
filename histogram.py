import sys

def histogram(word_text):
  dictionary = {}
  for word in word_text:
    if word in dictionary.keys():
      dictionary[word] += 1 
    else:
      dictionary[word] = 1
  return dictionary

def unique_words(word_text):
  dictionary = histogram(word_text)
  print("There are [" + str(len(dictionary)) + "] unique words in the text.")

def word_frequency(word, word_text):
  dictionary = histogram(word_text)
  if dictionary[word]:
    if dictionary[word] > 1:
      print("There are [" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
    else: 
      print("There is [" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
  else:
    print("Word was not found")

if __name__ == '__main__':
  file_name = sys.argv[1]
  word_check = sys.argv[2]
  f = open(file_name,'r', encoding='utf-8-sig')
  blog_text = f.read()
  clean_text = blog_text.replace(',','').replace('.','').replace('?','').replace("'",'').replace('"','').replace('-','')
  word_text = clean_text.split(' ')
  f.close()
  histogram(word_text)
  unique_words(word_text)
  word_frequency(word_check, word_text)