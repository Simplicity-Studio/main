# T573805 [语言月赛 202502] 披萨订单

X,Y,K = map(int,input().split())

delicious = []
for x in range(0,X+1):
    for y in range(1,Y+1):
        for k in range(0,K+1):
            delicious.append((x+y)^k)
mx = max(delicious)
# print(delicious)
print(mx)
i = 0
while max(delicious) == mx:
    delicious.remove(mx)
    i += 1
print(i)