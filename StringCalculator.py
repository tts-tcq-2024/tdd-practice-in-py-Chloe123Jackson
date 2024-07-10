import re
def add (word):
  if word == "":
    return 0
  else:
    return extract(word)

def extract(word):
  regex1 = re.compile('//.\n')
  regex2 = re.compile(',.,')
  regex3 = re.compile('./n.')
  matches1 = re.findall(regex1, word)
  matches2 = re.findall(regex2, word)
  matches3 = re.findall(regex3, word)

  if matches1!=[]:
    delimiter=matches1[0][2]
    word=word.replace(matches1[0],'')
    str_wordlist=word.split(delimiter)
    word_split=list(map(int, str_wordlist))
    for ele in word_split:
      word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
      t_sum=sum(word_split)
      return t_sum
  if matches2!=[]:
    str_wordlist=word.split(',')
    word_split=list(map(int, str_wordlist))
    for ele in word_split:
      word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
      t_sum=sum(word_split)
      return t_sum
  if matches3!=[]:
    word=word.replace('\n','')
    str_wordlist=word.split(',')
    word_split=list(map(int, str_wordlist))
    for ele in word_split:
      word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
      t_sum=sum(word_split)
      return t_sum
  if matches1==[] and matches2==[] and matches3==[]:
    str_wordlist=word.split(',')
    word_split=list(map(int, str_wordlist))
    for ele in word_split:
      word_split[word_split.index(ele)]={True: 0, False: ele} [ele>1000]
      t_sum=sum(word_split)
      return t_sum
  

# def check_delimiter(word):
#   regex1 = re.compile('//.\n')
#   regex2=  re.compile('.,.')
#   matches_custom=re.findall(regex1, word)
#   matches_normal=re.findall(regex2, word)
#   if matches_custom!=[]:
#     delimiter=matches_custom[0][2]
#     word=word.replace(matches_custom[0],'')
    
  
  
  
