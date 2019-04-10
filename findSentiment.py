from utils import commenters

# MUST READ THIS: https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f
def getTextSentiment(text):
        """
            Description:
                Given a string find its sentiment.

            Return:
                Return the polarity score.
        """

def getAverageSentiment(comments):
    """
        Description:
            The function takes in a list of strings and returns the average
            polarity for that list.

        Arguments:
            comments: a list of strings.
            Example:
                [
                    '🏃💭Leave em n tha rearview',
                    '💯',
                    'hi 💯',
                ]

        Return:
            Returns the average polarity of the list.
        """


if __name__ == '__main__':
    comments = [comment['text'] for comment in commenters]
    print(comments)
