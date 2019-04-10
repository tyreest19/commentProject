from  utils import commenters

# MUST READ: https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

def findWordFrequency(text):
    """
        Description:
            The function takes a sentence and creates a Frequency Distribution Plot for words
            used.
    """

def findCommentFrequency(comments):
    """
        Description:
            Given a list of strings creates a Frequency Distribution Plot for words
            used.
    """

if __name__ == '__main__':
    print('This is a test')
    comments = [comment['text'] for comment in commenters]
    print(comments)
    findWordFrequency('How many wood would a woodchuck chuck if a woodchuck could chuck wood?')
    findCommentFrequency(comments)
