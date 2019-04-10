from utils import commenters

def findNumberOfComments(commets):
    """
        Description:
            The function takes in a list comments containing a dictionary of
            userID, username, and text. Then returns a list of sets
            including a username and number of comments.

        Arguments:
            comments: a list of dictionaries containing the userID, username, and text.
            Example:
            [
                {'user_id': 3676188449, 'username': 'dosiafranklin', 'text': '🏃💭Leave em n tha rearview'},
                {'user_id': 9017020144, 'username': 'ultracurve', 'text': '💯'},
                {'user_id': 9017020144, 'username': 'ultracurve', 'text': 'hi 💯'},
            ]
        Return:
            Return a list of sets containing a username and their number of commets
            Example:
                [
                    ('jimbob', 1),
                    ('x_tyree', 2),
                ]
    """


def findTopCommenters(usernameAndComments):
    """
        Description:
            The function takes in a list of sets containing a username and comments.

        Arguments:
            usernameAndComments: a list of sets containing an username and number
            of comments.
            Example:
                [
                    ('jimbob', 1),
                    ('x_tyree', 2),
                ]

        Return:
            Return a list the list order from greatest to least number of comments.
                [
                    ('x_tyree', 2),
                    ('jimbob', 1),
                ]
    """


if __name__ == '__main__':
    print('Test Code')
    usernameAndComments = findTopCommenters(commenters)
    print(findTopCommenters(usernameAndComments))
