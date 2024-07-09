
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  str_wordlist=word.split(",")
  word_split=list(map(int, str_wordlist))
  t_sum=sum(word_split)
  return {True: t_sum-1000, False: t_sum} [t_sum>1000]
  
  
