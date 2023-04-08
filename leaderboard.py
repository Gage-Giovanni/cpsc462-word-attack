def addScore(name, score):
    file = open('scores.txt', 'a')
    file.write(name + ',' + str(score) + '\n')
    file.close()

def getSortedLeaders():
    with open('scores.txt', 'r') as score_file:
        score_dict = {}
        
        for line in score_file:
            name,score = line.strip().split(',')
            score_dict[name]=int(score)
    sorted_leaderboard = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_leaderboard
    
def printLeaderboard(sorted_leaderboard):
    for entry in sorted_leaderboard:
        print(f"{entry[0]:<12} {str(entry[1])}")