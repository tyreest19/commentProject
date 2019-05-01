import os
from datetime import datetime
from findSentiment import createSentimentGraph
from findSentiment import getTextSentiment
from getComments import get_comments
from getComments import createCSVFile
from topCommenters import getCommenters
from topCommenters import generateHist
username = 'x_tyree'
password = 'Imorehouse19st'
amountOfComments = 100
usernameOfPage = 'barackobama'
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
