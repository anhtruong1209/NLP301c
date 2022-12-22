import nltk


text = '''               
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samanthasize at the bus size.
'''
def freq_non_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    clean_list = [w for w in text if w.lower() not in stopwords] 
    freqdist = nltk.probability.FreqDist(clean_list)
    return freqdist.most_common(50)

a = freq_non_stopwords(text)
print(a)