# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true


n, x = map(int, input().split())
sub = [list(map(float, input().split())) for _ in range(x)]
for i in zip(*sub):
    print(i)
    print(sum(i)/len(i))
    