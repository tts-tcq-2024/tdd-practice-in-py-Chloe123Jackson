import re
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  regex = re.compile('//.\n')
  matches = re.findall(regex, word)
  if matches!=[]:
    delimiter=matches[0][2]
    word=word.replace(matches[0],'')
    str_wordlist=word.split(",")
    word_split=list(map(int, str_wordlist))
    for ele in word_split:
      word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
      t_sum=sum(word_split)
      return t_sum
  else:
    regex=re.compile('.,.')
    matches = re.findall(regex, word)
    if matches!=[]:
      delimiter=matches[0][2]
      word=word.replace(matches[0],'')
      str_wordlist=word.split(",")
      word_split=list(map(int, str_wordlist))
      for ele in word_split:
        word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
        t_sum=sum(word_split)
      return t_sum
    
  
  
  
