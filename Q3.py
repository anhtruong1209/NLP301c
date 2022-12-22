import nltk


text = '''               
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samanthasize at the bus size.
'''

from nltk.tokenize import WordPunctTokenizer
text = "Reset your password if you just can't remember your old one."
print("\nOriginal string:")
print(text)
result = WordPunctTokenizer().tokenize(text)
print("\nSplit all punctuation into separate tokens:")
print(result)