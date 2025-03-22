# T573806 [语言月赛 202502] 本俗妙手不如举手

n, k = map(int,input().split())
a = list(map(int,input().split()))

win = 0
for i in a:
    win += ((99-i) >= 50)
cnt = 0
for l in range(0,n-k+1):
    win2 = win
    for l2 in range(l,l+k):
        if 48 <= 99-a[l2] <= 49:
            win2 += 1
    if win2*2 > len(a):
        cnt += 1
print(cnt)