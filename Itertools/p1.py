# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations as P

inp = list(map(str, input().split()))
inp[0] = sorted(inp[0])
lst = list(P(inp[0], int(inp[1])))
for i in lst:
    for j in i:
        print(j, end="")
    print()
