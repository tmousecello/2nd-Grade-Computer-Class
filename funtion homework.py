# h841: 開根號計算器

import math
a = float(input())
x = math.sqrt(a)

if a % 1 == 0:
  print(int(x))
else:
  print(x)
  
# f208: GJ-a035: 位數

import math

a = input().split()
loga = math.log10(int(a[0]))
print(int(int(a[1])*loga//1+1))

# f618: 多數中最大的

a = input().split()
list_a = []
for i in a:
  list_a.append(float(i))
print(max(list_a))

# a024: 最大公因數(GCD)

import math
a = input().split()
gcd = math.gcd(int(a[0]),int(a[1]))
print(gcd)

# g825: 最小公倍數(LCM)

import math

while True:
  try:
    a = input().split()
    gcd = math.gcd(int(a[0]),int(a[1]))
    print(int(int(a[0])*int(a[1])/gcd))
  except Exception:
    break
    
  # d693: 最小公倍數

import math
while True:
  skip = int(input())  
  if skip == 0:
    break
  else:
    a = input().split()
    gcd = math.gcd(int(a[0]),int(a[1]))
    lcm = int(int(a[0])*int(a[1])/gcd)

    for i in range(2,len(a)):
      gcd = math.gcd(lcm,int(a[i]))
      lcm = int(lcm*int(a[i])/gcd)

    print(lcm)
    
# c202: 最大公因數(GCD)-TOI練習賽y7m5-4

import math
skip = input()
a = input().split()
gcd = math.gcd(int(a[0]),int(a[1]))

for i in range(3,len(a)):
  gcd = math.gcd(gcd, int(a[i]))

print(gcd)

10# c013: 00488 - Triangle Wave

def wave(h):
    for i in range(h):
        print(str(i)*i)
    for i in range(h,0,-1):
        print(str(i)*i)
    print("")

re = int(input())
asndf = input()
for i in range(re):
    a = int(input())
    f = int(input())
    for i in range(f):
      wave(a)

  # b513: 判斷質數-商競103

# 質數判斷
def check(n):
    sqrtn = int(n**0.5)
    final = ""
    if n > 1:
        for i in range (2,sqrtn+1):
            if n % i == 0:
                 final = "N"
                 break
    if final != "N":
      final = "Y"
    print(final)

a = int(input())
for i in range(a):
  check(int(input()))
