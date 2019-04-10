
import csv
import time
from InstagramAPI import InstagramAPI
from datetime import datetime

def get_comments(username, password, amount_of_comments, searched_user):

    until_date = '1990-03-31'
    count = amount_of_comments
    API = InstagramAPI(username, password)
    API.login()
    comments = []
    max_id = ""
    has_more_comments = True
    API.searchUsername(searched_user)
    user_id = API.LastJson["user"]["pk"]
    media = []
    API.getUserFeed(user_id, maxid=max_id)
    media_ids = [item['id'] for item in API.LastJson.get('items')]
    print(len(media_ids))
    for media_id in media_ids:
        while has_more_comments:
            _ = API.getMediaComments(media_id, max_id='')
            # comments' page come from older to newer, lets preserve desc order in full list
            for c in reversed(API.LastJson['comments']):
                comments.append(c)
            has_more_comments = API.LastJson.get('has_more_comments', False)
            # evaluate stop conditions
            if count and len(comments) >= count:
                comments = comments[:count]
                # stop loop
                has_more_comments = False
            if until_date:
                older_comment = comments[-1]
                dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
                # only check all records if the last is older than stop condition
                if dt.isoformat() <= until_date:

                    # keep comments after until_date
                    until_date = datetime.strptime(until_date, '%Y-%m-%d')
                    print(until_date)
                    comments = [
                        c
                        for c in comments
                        if datetime.utcfromtimestamp(c.get('created_at_utc', 0)) > until_date
                    ]
                    # stop loop
                    has_more_comments = False
                    print("stopped by until_date")
            # next page
            if has_more_comments:
                max_id = API.LastJson.get('next_max_id', '')
                time.sleep(2)
        has_more_comments = True
    comments = [
                {   'user_id': comment['user_id'],
                    'username': comment['user']['username'],
                    'text': comment['text']
                }
                for comment in comments
                ]
    return comments

def createCSVFile(listOfDicts):
    keys = listOfDicts[0].keys()
    with open('comments.csv', 'w', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(listOfDicts)

if __name__ == '__main__':
    comments = get_comments('x_tyree', 'Imorehouse19st', 1000, 'barackobama')
    print(comments)
    createCSVFile(comments)
