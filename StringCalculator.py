import re
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  
  word,delimiter=check_delimiter(word)
  str_wordlist=word.split(delimiter)
  word_split=list(map(int, str_wordlist))
  for ele in word_split:
    word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
  t_sum=sum(word_split)
  return t_sum  

def check_delimiter(word):
  regex1 = re.compile('//.\n')
  regex2 = re.compile('.\n.')
  matches1 = re.findall(regex1, word)
  matches2 = re.findall(regex2, word)
  delimiter=','
  
  if matches1!=[]:
    delimiter=matches1[0][2]
    word=word.replace(matches1[0],'')
  if matches2!=[]:
    word=word.replace('\n',',')
  return word,delimiter
    
  
  
  
