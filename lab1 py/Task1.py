word = input('Enter a word: ')
result=""
word = word.lower()
for letter in word:
  if(letter not in ["a","e",'i',"o","u"]):
    result += letter
print(result)


