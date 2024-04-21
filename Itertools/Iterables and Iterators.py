# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations as c

n = int(input())
lst = list(map(str, input().split()))
k = int(input())
combi = list(c(lst, k))
cnt = 0
for i in combi:
    if "a" in i:
        cnt += 1
print(cnt / len(combi))