# T573804 [语言月赛 202502] 随机数

import math

n,L,R = map(int,input().split())

lst = []
avg = math.floor(L/n)
for i in range(n):
    lst.append(avg)
i = 0
d = L - sum(lst)
while d > 0:
    if lst[i] + d >= 10**6:
        lst[i] = 10**6
        i += 1
    else:
        lst[i] += d
    d = L - sum(lst)

print(" ".join(map(str, lst)))