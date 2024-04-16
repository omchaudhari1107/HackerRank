if __name__ == '__main__':
    lst,scores,names=list(),list(),list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        scores.append(score)
    scores=list(set(sorted(scores)))  
    print(scores)
    for i in lst:
        if i[1]==scores[1]:
            names.append(i[0])
    names=sorted(names)
    for i in names:
        print(i)      
        