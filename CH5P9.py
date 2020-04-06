import random
hedges = ("Hello. ", "How are you? ", "I would like to order a drink. ")
qualifiers = ("I feel uneasy. ", "Why do you do this? ", "I cannot continue like this ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "you":"I", "your":"my", "yours":"mine"}
def reply(sentence):
  prob = random.randint(1,4)
  if prob == 1:
    random.choice(hedges)
  else:
    return random.choice(qualifiers) + changePerson(sentence)
def changePerson(sentence):
  words = sentence.split()
  replyWords = []
  for word in words:
    replyWords.append(replacements.get(word, word))
  return " ".join(replyWords)
def main():
  print("You must leave immediately.")
  print("Can you not see the situation we are in?")
  while True:
    sentence = input("\n>> ")
    if sentence.lower() == "quit":
      print("You ruined us.")
      break
    print(reply(sentence))
if __name__ == "__main__":
  main()
