inp=input()
hc=0
score=0
for i in inp:
    if i=="H" or "h":
        hc+=1
        score+=2
        if hc==3:
            break
        else:
            score-=1
            hc=0
print(score)            