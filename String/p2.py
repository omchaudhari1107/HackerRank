def Convert(sets):
    string=''
    for i in sets:
        string+=i
    return string
def merge_the_tools(s, k):
    cnt=0
    for _ in range(len(s)):
        x=list(s[cnt:k+cnt])
        sets=sorted(set(x), key=x.index)
        print(Convert(sets)) 
        cnt+=k
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)