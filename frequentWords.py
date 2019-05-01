#Imported libraries
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def findCommentFrquency(comments, fileName):
    lst = []
    stop_words=set(stopwords.words("english"))
    additional_stop_words = set([";", ",", "’", ".", "?", ":", "`", "its", ",","\'", '@', '*', '!'])
    stop_words.update(additional_stop_words)
    for i in comments:
        idv_words = word_tokenize(i.lower())
        for i in idv_words:
            if i not in stop_words:
                lst.append(i)
    #print(lst)
    fdist = FreqDist(lst)
    words = []
    frequencies = []
    limit = 50
    for word, frequency in fdist.most_common(limit):
        words.append(word)
        frequencies.append(frequency)
    fig = plt.figure(figsize=(100, 50))
    ax = plt.subplot(111)
    ax.bar(words, frequencies) #label='$y = numbers')
    plt.title('Most Common Words')
    plt.xlabel('Words', fontsize=15, labelpad=20)
    plt.ylabel('Frequency', fontsize=15, labelpad=20)
    fig.savefig(fileName)

if __name__ == '__main__':
    pass
