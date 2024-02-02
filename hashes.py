def hashed(key):  
  h = (sum(ord(character) for character in str(key)))*100000000/47
  h = str(round(h))
  
  return h[:7]