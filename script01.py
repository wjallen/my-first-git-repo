
# this script prints the first five lines of words file

words = []

with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines() 

words.sort(key=len, reverse=True) 

print(words[:5])

