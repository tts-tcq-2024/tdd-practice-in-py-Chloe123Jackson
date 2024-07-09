
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  str_wordlist=word.split(",")
  word_split=list(map(int, str_wordlist))
  for ele in word_split:
    if ele > 1000:
        word_split[word_split.index(ele)]=0
  t_sum=sum(word_split)
  return t_sum
  
  
  
