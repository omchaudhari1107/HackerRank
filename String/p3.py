# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

def Sorted_set(s):
    x = list(s)
    sets = sorted(set(x), key=x.index)
    return list(sets)


if __name__ == "__main__":
    s = "aabbbccde"
    txt, dic = "", dict()
    lst = Sorted_set(s)
    for i in lst:
        cnt = 0
        for j in range(len(s)):
            if i == s[j]:
                cnt += 1
        dic.update({i: cnt})
    sorted_l = sorted(dic.values(),reverse=True)
    sorted_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    for i,j in sorted_dic:
        if j > sorted_l[len(sorted_l)-1]:
            print(i,"",j)
    # lst = sorted(dic.values(),reverse=True)

