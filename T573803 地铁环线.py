# T573803 [语言月赛 202502] 地铁环线

n,start,tar = map(int,input().split())
if tar >= start:
    left = n-tar+start
    right = tar - start
else:
    left = start - tar
    right = n-start+tar
if left == right:
    print("\"Wonderful\"")
elif right < left:
    print("Clockwise Loop")
else:
    print("Counter-clockwise Loop")