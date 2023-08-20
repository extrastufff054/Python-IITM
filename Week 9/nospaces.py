f = open('insults.txt', 'r')

paragraph_without_spaces = f.read().replace(' ', '')

print(paragraph_without_spaces)
f.close()

f = open('insults.txt', 'w')
f.write(paragraph_without_spaces)   