import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def getTextSentiment(comments):
    sentimentAndDate = []
    for comment in comments:
        compoundScore = analyser.polarity_scores(comment['text'])['compound']
        sentimentAndDate.append((compoundScore, comment['dateUTC']))
    return sentimentAndDate

def createSentimentGraph(sentimentAndDate, fileName):
    figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
    utcDates = []
    sentimentScore = []
    print(len(sentimentAndDate))
    for i in range(len(sentimentAndDate)):
      utcDates.append(sentimentAndDate[i][1])
      sentimentScore.append(sentimentAndDate[i][0])
    plt.plot(utcDates, sentimentScore)
    plt.savefig(fileName)

def getAverageSentiment(comments):
    """
            Description:
                The function takes in a list of strings and returns the average
                polarity for that list.

            Arguments:
                comments: a list of strings.
                Example:
                    [
                        'Leave em n tha review',
                        'hey'
                        'whats up',
                    ]
            Return:
                Returns the average polarity of the list.
    """
    sum_polarity = 0
    for strings in comments:
        sum_polarity += getTextSentiment(strings)
    return sum_polarity/len(comments)

if __name__ == '__main__':
    pass
