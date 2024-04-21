# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
import itertools as it
k,m=map(int,input().split())

max_ele=0
combi_list = [list(map(int, input().split()[1:])) for _ in range(k)]
combi=it.product(*combi_list)
     
for i in combi:
    result = sum(x**2 for x in i) % m
    max_ele=max(max_ele,result)
print(max_ele) 
