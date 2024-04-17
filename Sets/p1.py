# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
n=input()

arr=list(map(int, n.split()))[0]
n=list(map(int, n.split()))[1]

ele=input()
ele=list(map(int, ele.split()))

A=input()
A=list(map(int, A.split()))

B=input()
B=list(map(int, B.split()))
happy=0

for i in ele:
    if i in A:
        happy+=1
    elif i in B:
        happy-=1
print(happy)