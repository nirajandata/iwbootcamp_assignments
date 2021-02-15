def firstval(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  print(str1)

  str1 = char + str1[1:]
   
  return str1

print(firstval('restart'))
