# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

N = int(input())
integers = list(map(int, input().split()))
print(all(x > 0 for x in integers) and any(str(x) == str(x)[::-1] for x in integers))