#1
conjuctives = []
with open('vocab.txt', "r", encoding = "utf-8") as f:
    words = f.readlines()

for i in range(len(words)):
    countw = words[i]
    conj = countw.find('союз')
    if conj != -1:
        conjuctives.append(words[i])

print(*conjuctives)

#2
words =[]
with open('vocab.txt', "r", encoding = "utf-8") as f:
    text = f.read()
    words = text.split('\n')
f = []
ipm = 0 
word = ''
gr = ''
count_ipm = ''

for i in range(len(words)):
    if 'сущ' in words[i] and 'жен' in words[i]:
       f.append(words[i])
       word,gr,count_ipm = words[i].split(' | ')
       ipm += float(count_ipm)
for i in range(len(f)):
    print(f[i] + ',')
print(ipm)

#for line in lines: 
     line = line.split (' | ')
    gr = line[1]
    if 'ед' in gr and 'сущ' in gr and 'жен' in gr and 'жен' in gr:
        nouns.append(line[0])
        ipm += float(line[-1])
    print(ipm)
    print(*nouns, sep = ',')

#3   не дописала 
k = 0
words = []
word = input()
while word:
    words.append(word)
    k += 1
    word = input()
with open('vocab.txt', "r", encoding = "utf-8") as f:
    text = f.read()           
    lines = text.split('\n')
for i in range(len(words)):
    k = 0
if words[i].count[' | '] == 2:
    word,gr,count_ipm = word[i].split(' | ')
    if words[i] == word.strip(' ')
    
    
    for line in f: 
        word = line.split (' | ') [0] 
        if word in words: 
            print(line.split (' | ') 
                  
     for word in words: 
                  for line in f:
                  w = line.split (' | ')
                  if word 
    
     
