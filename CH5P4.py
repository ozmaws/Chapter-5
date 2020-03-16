import random
def getWords(filename):
  input_file = open(filename, "r")
  wordList = []
  for line in input_file:
    for word in line.split():
      wordList.append(word)
  input_file.close()
  return tuple(wordList)
adjectives = getWords("adjectives.txt")
articles = getWords("articles.txt")
conjunction = getWords("conjunctions.txt")
nouns = getWords("nouns.txt")
prepositions = getWords("prepositions.txt")
verbs = getWords("verbs.txt")
def sentence():
  return nounPhrase() + " " + verbPhrase() + " " + conjunctionPhrase()
def nounPhrase():
  return random.choice(articles) + " " + adjective() + random.choice(nouns)
def verbPhrase():
  return random.choice(verbs) + " " + nounPhrase() + prepositionalPhrase()
def prepositionalPhrase():
  if random.randint(0,1) == 0:
    return " " + random.choice(prepositions) + " " + nounPhrase()
  else:
    return ""
def conjunctionPhrase():
  if random.randint(1,10) <= 3:
    return random.choice(conjunction) + " " + nounPhrase()
  else:
    return ""
def adjective():
  if random.randint(1,10) <= 8:
    return random.choice(adjectives) + " "
  else:
    return ""
def main():
  number = int(input("Number of sentences: "))
  for count in range(number):
    print(sentence())
if __name__ == "__main__":
  main()
