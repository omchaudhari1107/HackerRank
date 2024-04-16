import sys
def Recur(n,sum):
    sys.setrecursionlimit(1000000000)
    if n % 3 == 0 or n % 5 == 0:
        sum += n
    n-=1
    return Recur(n,sum)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(Recur(n,0))
        # sum = 0
        # for i in range(n):
        #     if i % 3 == 0 or i % 5 == 0:
        #         sum += i
        # print(sum)
