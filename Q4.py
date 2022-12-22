import nltk


text = '''               
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samanthasize at the bus size.
'''

from nltk.corpus import wordnet
list  = []
text1 = "John lives in Canada"
text2 = "James lives in America, through he's not from there"
list1 = text1.split(" ")
list2 = text2.split(" ")


for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1)
        wordFromList2 = wordnet.synsets(word2)
        if wordFromList1 and wordFromList2: #Thanks to @alexis' note
            s = wordFromList1[0].wup_similarity(wordFromList2[0])
            list.append(s)
            
s = 0
for i in list:
    s += i

print(1- s/len(list))
    