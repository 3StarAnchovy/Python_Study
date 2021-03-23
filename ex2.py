score = [90,80,70,50,100]
sum = 0
for i in range(len(score)):
    sum+=score[i]
    if score[i] > 70:
        print(i,"번째는 패스\n") # , +
    else:
        print(i,"번째는 나락\n")
print("avg : ",sum/len(score));