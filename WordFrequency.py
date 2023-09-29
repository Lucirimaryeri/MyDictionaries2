wrd_frequency = {}

#open sometext.txt
sometext = open('sometext.txt', 'r')

#split to words
words = sometext.read().split()

for word in words:
    word = word.strip('.,!?":;').lower() 
    if word in wrd_frequency:
        wrd_frequency[word] += 1
    else:
        wrd_frequency[word] = 1

#close txt file
sometext.close()

#print(wrd_frequency)
for key, value in wrd_frequency.items():
    print(f'{key}: {value}')
