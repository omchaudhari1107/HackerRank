# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict,Counter

n = int(input())
od = OrderedDict()
lst=list()
for i in range(n):
    string=' '
    items = list(map(str, input().split()))
    lst.append(int(items[len(items)-1]))
    cnt = Counter(lst)
    od[string.join(items[0:len(items) - 1])] = int(items[len(items)-1]) * cnt[int(items[len(items)-1])]
    del string

for key, value in od.items():
    print('{} {}'.format(key,value))
