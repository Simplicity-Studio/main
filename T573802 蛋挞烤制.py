# T573802 [语言月赛 202502] 蛋挞烤制

import math

Vegg,Vmilk,Vtart = map(int,input().split())
e,m,t = map(int,input().split())

Vsum = e*Vegg + m*Vmilk
n = math.ceil(Vsum/Vtart)
print(math.ceil(n/t))