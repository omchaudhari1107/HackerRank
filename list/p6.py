# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

def Generate(x,y,z,n):
    lst=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n: 
                    lst.append([i,j,k])
    print(lst)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    Generate(x,y,z,n)