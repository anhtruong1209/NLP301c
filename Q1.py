text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samanthasize at the bus size.
'''
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
token_word = word_tokenize(text)
a = [w for w in token_word if w.endswith('ize')]
print(a)