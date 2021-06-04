introductions = input('About You: ')
charactercount = 0
wordcount = 1
for i in introductions:
    charactercount = charactercount+1
    if i == ' ':
        wordcount = wordcount+1
print('No. of words in the strings')
print(wordcount)
print('No. of characters in the strings')
print(charactercount)