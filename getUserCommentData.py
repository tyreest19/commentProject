import os
from datetime import datetime
from findSentiment import createSentimentGraph
from findSentiment import createSentimentPieGraph
from findSentiment import getTextSentiment
from frequentWords import findCommentFrquency
from getComments import get_comments
from getComments import createCSVFile
from topCommenters import getCommenters
from topCommenters import generateHist

username = 'x_tyree'
password = 'Imorehouse19st'
amountOfComments = 100
usernameOfPage = input('Please input instagram name you are searcing for'
                        'without the \'@\' sign: ')
currentDT = datetime.now()
currentDT = currentDT.strftime('%d-%m-%Y %H:%M:%S.%f').lstrip("   ").replace(" ", "_")
directoryName = usernameOfPage + '_' + currentDT

os.makedirs(directoryName) # Create Folder
comments = get_comments(username, password, amountOfComments, usernameOfPage)
createCSVFile(comments, directoryName) # Create CSV File

# ##### Graph Top Commenters ######
topNumberOfCommenters = 10
commenters = getCommenters(comments, topNumberOfCommenters)

# Gets a list of tuples Example [('username', 'number of commenters')]
fileName = directoryName + '/' + 'topCommenters'
generateHist(commenters, fileName)

# ##### Find Sentiment ######
sentimentAndDate = getTextSentiment(comments)
fileName = directoryName + '/' + 'radicalizationChart'
createSentimentGraph(sentimentAndDate, fileName)
fileName = directoryName + '/' + 'radicalizationPieChart'
createSentimentPieGraph(sentimentAndDate,fileName)

# ##### Graph Top Commenters ######
commentsText = [comment['text'] for comment in comments]
fileName = directoryName + '/' + 'wordFrequencyChart'
commenters = findCommentFrquency(commentsText, fileName)
