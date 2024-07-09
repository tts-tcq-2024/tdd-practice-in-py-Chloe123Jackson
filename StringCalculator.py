
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  str_wordlist=word.split(",")
  word_split=list(map(int, str_wordlist))
  return(sum(word_split))
  
  
