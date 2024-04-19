# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations

inp = list(map(str, input().split()))
lst = sorted(list(inp[0]))
n_lst = list()
for i in range(1, int(inp[1]) + 1):
    n_lst.append(list(combinations(lst, i)))

for i in n_lst:
    for j in i:
        for k in j:
            print(k, end="")
        print()
