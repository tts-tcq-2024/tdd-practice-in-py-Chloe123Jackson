import re
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  
  word,delimiter=check_spec_char(word)
  str_wordlist=word.split(delimiter)
  word_split=list(map(int, str_wordlist))
  try:
    if (ele<0 for ele in word_split):
      raise NegativesNotAllowed
  except NegativesNotAllowed:
    print(list(ele for ele in word_split if ele<0))
  for ele in word_split:
    word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
  t_sum=sum(word_split)
  return t_sum  

def check_spec_char(word):
  regex = re.compile('//.*\n')
  matches = re.findall(regex, word)
  delimiter=','
  if matches!=[]:
    index_1 = matches[0].find('//')
    index_2 = matches[0].find('\n',index_1)
    delimiter=matches[0][index_1+2:index_2]
    word=word.replace(matches[0],'')
  word=word.replace('\n',',')
  return word,delimiter

class NegativesNotAllowed(Exception):
  "Raised when negative value is provided as input"
  pass



    
  
  
  
