import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def getCommenters(commentList, topNumberOfCommenters):
    res = []

    for i in commentList:
        username = i['username']
        x = 0
        for i in res:
            if i[0] == username:
                i[1] = i[1] + 1
                x = 1
                break
        if x == 0:
            res.append([username, 1])
    res = [tuple(i) for i in res]

    for i in range(len(res)):
        for j in range(len(res)):
            if res[i][1] > res[j][1]:
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
    res = res[:topNumberOfCommenters]
    return res

def generateHist(listTuples, fileName):
    figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
    word = []
    frequency = []
    for i in range(len(listTuples)):
      word.append(listTuples[i][0])
      frequency.append(listTuples[i][1])
    plt.bar(word, frequency, color='r')
    plt.savefig(fileName)

if __name__ == '__main__':
    cDict = [{'user_id': 3676188449, 'username': 'jimbob', 'text': '*emoji*Leave em n tha rearview'},
            {'user_id': 9017020144, 'username': 'x_tyree', 'text':'*emoji*' },
            {'user_id': 9017020144, 'username': 'x_tyree', 'text': 'hi *emoji*'}]

    listTuples =  getCommenters(cDict)
    print(listTuples)
    generateHist(listTuples, 'testCscore2')
