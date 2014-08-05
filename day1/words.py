#file = open('words.txt')

for line in file:
  word = line.strip()
  print word
  
def has_no_e(word):
   return "e" not in word
   
def uses_only(word, available):
   for letter in word:
     if not letter in available:
       return False
     else:
       return True
    
def uses_all(word, available):
   return uses_only(available, word)
    
def is_abecedarian(word):
     return "".join(sorted(word)) == word
