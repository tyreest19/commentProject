import matplotlib
import datetime as dt
import matplotlib.dates as md
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def getTextSentiment(comments):
    """
            Description:
                Takes a dictionary containing commnets and other data, then
                returns a tuple of the comments sentiment score and dattime object
            Arguments:
                sentimentAndDate: a list of tuples.

            Returns:
                A list of tuples contains sentiment score and datetime object
                Example:
                    [
                        (0.567, 2019-05-01 15:55:44),
                        (-0.567, 2019-05-01 15:55:44)
                    ]
    """
    sentimentAndDate = []
    for comment in comments:
        compoundScore = analyser.polarity_scores(comment['text'])['compound']
        sentimentAndDate.append((compoundScore, comment['dateUTC']))
    return sentimentAndDate

def createSentimentGraph(sentimentAndDate, fileName):
    """
            Description:
                Takes a list of tuples containing Sentiment Score and datetime
                object, then creates a graph.

            Arguments:
                sentimentAndDate: a list of tuples.
                    Example:
                        [
                            (0.567, 2019-05-01 15:55:44),
                            (-0.567, 2019-05-01 15:55:44)
                        ]
    """
    figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
    utcDates = []
    sentimentScore = []
    for i in range(len(sentimentAndDate)):
      utcDates.append(sentimentAndDate[i][1])
      sentimentScore.append(sentimentAndDate[i][0])
    plt.subplots_adjust(bottom=0.2)
    plt.xticks( rotation=25 )
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.xlabel('UTC Date Time', fontsize=15, labelpad=20)
    plt.ylabel('Sentiment Score', fontsize=15, labelpad=20)
    plt.title('Radicalization Chart', fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
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
