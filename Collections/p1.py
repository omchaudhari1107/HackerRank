# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter

n = int(input())
size = list(map(int, input().split()))
customer = int(input())
cnt = dict(Counter(size))
total_cost = 0
for i in range(customer):
    s, cost = map(int, input().split())
    if s in cnt.keys():
        if cnt[s] > 0:
            cnt[s] -= 1
            total_cost += cost

print(total_cost)
