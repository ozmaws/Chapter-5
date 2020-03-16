import random
def getWords(filename):
  input_file = open(filename, "r")
  wordList = []
  for line in input_file:
    for word in line.split():
      wordList.append(word)
  input_file.close()
  return tuple(wordList)
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
prepositions = getWords("prepositions.txt")
verbs = getWords("verbs.txt")
def sentence():
  return nounPhrase() + " " + verbPhrase()
def nounPhrase():
  return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
  return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
def prepositionalPhrase():
  return random.choice(prepositions) + " " + nounPhrase()
def main():
  number = int(input("Enter the number of sentences: "))
  for count in range(number):
    print(sentence())
if __name__ == "__main__":
  main()
