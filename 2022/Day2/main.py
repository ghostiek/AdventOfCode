import helper

with open("data.txt", "r") as file:
    txt = file.readlines()
txt = [elem.replace("\n", "") for elem in txt]

RPS_map = {"A":"Rock", "B":"Paper","C":"Scissors", "X":"Rock", "Y":"Paper","Z":"Scissors"}
scores = {"Rock":"1", "Paper":"2", "Scissors":"3"}

total_score = 0
for line in txt:
    tmp_line = line
    tmp_line = helper.replace_map(tmp_line, RPS_map)
    output1 = tmp_line.split(" ")[0]
    output2 = tmp_line.split(" ")[1]
    if output2 == output1:
        score1 = 3
    elif output1 == "Rock":
        if output2 == "Paper":
            score1 = 6
        else:
            score1 = 0
    elif output1 == "Paper":
        if output2 == "Scissors":
            score1 = 6
        else:
            score1 = 0
    #Scissors
    else:
        if output2 == "Rock":
            score1 = 6
        else:
            score1 = 0

    tmp_line = helper.replace_map(tmp_line, scores)
    score2 = int(tmp_line[2])
    total_score += score1 + score2
print(total_score)

# Part 2
with open("data.txt", "r") as file:
    txt = file.readlines()
txt = [elem.replace("\n", "") for elem in txt]

total_score=0
for line in txt:
    tmp_line = line
    tmp_line = helper.replace_map(tmp_line, RPS_map)
    output1 = tmp_line.split(" ")[0]
    output2 = tmp_line.split(" ")[1]
    # Need to lose
    if output2 == "Rock":
        score1 = 0
        if output1 == "Rock":
            score2 = 3
        elif output1 == "Paper":
            score2 = 1
        else:
            score2 = 2
    # Need to tie
    elif output2 == "Paper":
        score1 = 3
        if output1 == "Rock":
            score2 = 1
        elif output1 == "Paper":
            score2 = 2
        else: score2 = 3
    # Need to win
    else:
        score1=6
        if output1=="Rock":
            score2 = 2
        elif output1=="Paper":
            score2 = 3
        else:
            score2=1
    total_score += score1 + score2
print(total_score)