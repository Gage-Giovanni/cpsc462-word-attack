def addScore(name, score):
    file = open('scores.txt', 'a')
    file.write(name + ',' + str(score) + '\n')
    file.close()

def getSortedLeaders():
    with open('scores.txt', 'r') as score_file:
        score_list = []
        
        for line in score_file:
            name,score = line.strip().split(',')
            score_list.append({"name":name, "score":int(score)})
    sorted_leaderboard = sorted(score_list, key=lambda x:x['score'], reverse=True)
    return sorted_leaderboard
    
def printLeaderboard():
    sorted_leaderboard = getSortedLeaders()
    for entry in sorted_leaderboard:
        print(entry['name'] + " - " + str(entry['score']))