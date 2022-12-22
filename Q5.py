import nltk
from nltk.book import * 
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
s  =  text1
a = [w for w in s if w.endswith('ize')]
b = [w for w in s if 'z' in w]
c = [w for w in s if 'pt' in w]
d = [w for w in s if w.istitle()]


# 28. Define a function percent(word, text) ** that calculates how often a given word occurs in a text, and expresses the result as a percentage.**
def percent(word, text):
    return 100 * text.count(word) / len(text)



text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''
print("\nOriginal string:")
print(text)
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
token_sentence = sent_tokenize(text)
token_word = word_tokenize(text)
print("\nSentence-tokenized copy in a list:")
print(token_sentence)
print("\nWord-tokenized copy in a list:")
print(token_word)
print("\nRead the list:")
for s in token_sentence:
    print(s)

text2 = '''Robert Langdon is a famous character in variuous books and movies.'''
nltk_results = ne_chunk(pos_tag(word_tokenize(text2)))
a = []
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        a.append(name)
listToStrName = ' '.join([str(elem) for elem in a])
for s in token_sentence:
    print(s)
    

# Q3
import re
def doubleConsonants(currStr):
    vowelList = ['a','e','i','o','u','y']
    newStr = ""
    consList = [subStr+subStr if re.match(r"[^\W\daeiouy]",subStr) else subStr for subStr in currStr]
    return newStr.join(consList)

dStr = doubleConsonants(text2)
print(dStr)