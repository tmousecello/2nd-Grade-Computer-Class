# hello, world

print("hello world")

# This is a book. 

print("This is a book.\nThat is a pen.\nI am a student.")

#　中華民國萬歲！

print(int(input())-1911)

# 簡易加法

a=str(input()).split()
print(int(a[0])+int(a[1]))

# 時間換算(一)

a=str(input()).split()
print(int(a[0])*60+int(a[1]))

# 時間換算(二)

min = int(input())
print(min//60, min%60)

# 年齡推算

G = int(input())
bigG = G+3
Bl = G*2-5
print(Bl//10*10+bigG%10)

# 奇數與偶數

if int(input())%2==0:
  print("EVEN")
else:
  print("ODD")
  
 # 貨比三家

a=input().split()
a.sort()

print(a[0])

# 閏年判斷 - 1

year = int(input())
if year % 4 == 0 and year % 100 != 0:
  print("YES")
elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
  print("YES")
else:
  print("NO")

# 閏年判斷 - 2

i = input()
if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
    print("YES")
else:
    print("NO")
    
# 閏年判斷 - 3 

import calendar as ca
year = int(input())
if ca.isleap(year) == True:
  print("YES")
else:
  print("NO")

# 我討厭偶數

a = int(input())
while True:
  if a%2 == 0:
    a/=2
  else:
    print(int(a))
    break

# 細菌繁殖

a = input().split()
min = int(0)
b = int(a[0])

while True:
  if b >= int(a[1]):
    print(min)
    break
  else:
    b*=3
    min+=1
    
# 3N+1 - 1

ls = []
ls.append(int(input()))
while True:
  if ls[-1] == 1:
    print(len(ls))
    break
  elif ls[-1]%2 == 0:
    ls.append(ls[-1]/2)
  else:
    ls.append(ls[-1]*3+1)

#3N+1 - 2

t = int(input())
i = 1
while int(t) != 1:
    if t % 2 == 1:
        t = 3*t + 1
    else:
        t /= 2
    i += 1
print(i)
    
# 所有位數和 - 1

num = input()
sum = int(0)
for i in num:
  sum += int(i)
print(sum)

# 所有位數和 - 2

k = input()
i = int(k)
l = len(k)
n = 0
for j in range(l):
    n += (i % (10 ** (j + 1))) / (10 ** j)
    i -= i % (10 ** (j + 1))
print(int(n))

# 一千遍我愛你 - 1

for i in range(int(input())):
  print("I love you.")

# 一千遍我愛你 - 2

i = int(input())
print("I love you.\n" * i)

# 倒數計時 - 1

c = ""
for i in range(int(input()), -1, -1):
  c += str(i)
  c += " "
print(c)

# 倒數計時 - 2

i = int(input())
while i >= 0:
    print("{} ".format(i), end='')
    i -= 1

# P(N,R) - 1
# 本解法邪教

a = input().split()
num1 = a[0]
num2 = a[1]
sum = ""

for i in range(int(num2)):
  sum += str(int(a[0])-int(i))
  sum += "*"

sum = sum.rstrip("*")
print(eval(sum))

# P(N,R) - 2

from math import factorial as f
i = input().split()
n = int(i[0])
r = int(i[1])
print(int(f(n)/f(n-r)))

# 連續整數相加 - 1

a = input().split()
sum = 0
b = ""
for i in range(int(a[0]), int(a[1])+1):
  sum += i
  b += str(i)
  b += "+"

b = b.rstrip("+")
b += "="
b += str(sum)
print(b)

# 連續整數相加 - 2

ip = input().split()
k = int(ip[0])
n = int(ip[1])
x = 0
for i in range(k, n+1):
    print(i, end='')
    x += i
    if i != n:
        print("+", end='')
    else:
        print("=", end='')
print(x)

# 格瑞哥里的煩惱 (1行版) - 1

year = int(input())
if year % 4 == 0 and year % 100 != 0:
  print("a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
  print("a leap year")
else:
  print("a normal year")

# 格瑞哥里的煩惱 (1行版) - 2

i = input()
if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
    print("a leap year")
else:
    print("a normal year")
    
# 格瑞哥里的煩惱 (1行版) - 3

import calendar as ca
year = int(input())

if ca.isleap(year) == True:
  print("a leap year")
else:
  print("a normal year")

# 格瑞哥里的煩惱 (t行版) - 1

a = int(input())
for i in range(a):
  year = int(input())
  if year % 4 == 0 and year % 100 != 0:
    print("a leap year")
  elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
    print("a leap year")
  else:
    print("a normal year")

 # 格瑞哥里的煩惱 (t行版) - 2
    
k = int(input())
for j in range(k):
    i = int(input())
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")
        
# 格瑞哥里的煩惱 (t行版) - 3

import calendar as ca

a = int(input())
for i in range(a):
  year = int(input())
  if ca.isleap(year) == True:
    print("a leap year")
  else:
    print("a normal year")

# 格瑞哥里的煩惱 (0尾版) - 1

while True:
  year = int(input())
  if year == 0:
    break
  else:
    if year % 4 == 0 and year % 100 != 0:
     print("a leap year")
    elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
     print("a leap year")
    else:
     print("a normal year")

# 格瑞哥里的煩惱 (0尾版) - 2

while True:
    i = int(input())
    if i == 0:
        break
    elif ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")
        
# 格瑞哥里的煩惱 (0尾版) 邪教版

import calendar as ca
while True:
  year = int(input())
  if year == 0:
    break
  else:
    if ca.isleap(year) == True:
      print("a leap year")
    else:
      print("a normal year")

# 格瑞哥里的煩惱 (EOF版) - 1

while True:
  try:
    year = int(input())
    if year % 4 == 0 and year % 100 != 0:
      print("a leap year")
    elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
      print("a leap year")
    else:
      print("a normal year")
  except EOFError:
    break

# 格瑞哥里的煩惱 (EOF版) - 2
    
while True:
    try:
        i = int(input())
    except Exception: # I'm lazy. So?
        break
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")
        
# 格瑞哥里的煩惱 (EOF版) - 3

import calendar as ca
while True:
  try:
    year = int(input())
    if ca.isleap(year) == True:
      print("a leap year")
    else:
      print("a normal year")
  except EOFError:
    break

# 格瑞哥里的煩惱 (Case版) - 1

a = int(input())
for i in range(a):
  year = int(input())
  if year % 4 == 0 and year % 100 != 0:
    print("Case", str(i+1)+":", "a leap year")
  elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
    print("Case", str(i+1)+":", "a leap year")
  else:
    print("Case", str(i+1)+":", "a normal year")

# 格瑞哥里的煩惱 (Case版) - 2

k = int(input())
for j in range(k):
    i = int(input())
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("Case {}: a leap year".format(j+1))
    else:
        print("Case {}: a normal year".format(j+1))
        
 # 格瑞哥里的煩惱 (Case版) - 3

import calendar as ca
a = int(input())
for i in range(a):
  year = int(input())
  if ca.isleap(year) == True:
    print("Case", str(i+1)+":", "a leap year")
  else:
    print("Case", str(i+1)+":", "a normal year")

# 77乘法表 - 1
# 本題解法邪教

print("""1*1=1\t1*2=2\t1*3=3\t1*4=4\t1*5=5\t1*6=6\t1*7=7
2*1=2\t2*2=4\t2*3=6\t2*4=8\t2*5=10\t2*6=12\t2*7=14
3*1=3\t3*2=6\t3*3=9\t3*4=12\t3*5=15\t3*6=18\t3*7=21
4*1=4\t4*2=8\t4*3=12\t4*4=16\t4*5=20\t4*6=24\t4*7=28
5*1=5\t5*2=10\t5*3=15\t5*4=20\t5*5=25\t5*6=30\t5*7=35
6*1=6\t6*2=12\t6*3=18\t6*4=24\t6*5=30\t6*6=36\t6*7=42
7*1=7\t7*2=14\t7*3=21\t7*4=28\t7*5=35\t7*6=42\t7*7=49""")

# 77乘法表 - 2 

for i in range (1,8):
    for j in range (1,8):
        print("{}*{}={}\t".format(i,j,i*j), end='')
    print('\n')

# 數字三角形 - 1

x = 0
z = 1
r = 1
for x in range(1,int(input())+1):
  print(str(x)*r)
  z += 1
  x += 1
  r += 1
  
# 數字三角形 - 2
  
n = int(input())
for i in range (1,n+1):
        print("{}".format(i)*i)

# 數字金字塔 - 1

a = int(input())
z = a
r = 0

for i in range(1,a+1):
  z -= 1
  r += 2
  print('_'*z + str(i)*(r-1))

# 數字金字塔 - 2  
  
n = int(input())
for i in range (1,n+1):
        print("_"*(n-i),end='')
        print("{}".format(i)*(2*i-1))

# 質數判斷

n = int(input())
sqrtn = int(n**0.5)
if n >1:
    for i in range (2,sqrtn+1):
        if n % i == 0:
            print("NO")
            exit(0)
print("YES")

# 最大公因數 - 1
# 本題解法邪教

import math
a = input().split()
print(math.gcd(int(a[0]), int(a[1])))

# 最大公因數 - 2

num = input().split(' ')
a = int(num[0])
b = int(num[1])
def gcd(c, d):
    if c+d != c or d:
        return gcd(d, c%d)
    else:
        print(c+d)
gcd(a,b)

# 陶陶摘蘋果 - 1

apple_high = input().split()
apple_count = 0
tow=int(input())+30

for i in apple_high:
  if int(i) <= tow:
    apple_count += 1

print(apple_count)

# 陶陶摘蘋果 - 2

h = input().split(' ')
l = int(input())
n = 0
for i in range(10):
    a = int(h[i])
    if a <= l + 30:
        n += 1
print(n)

# Box of Bricks - 1

count = 0

while True:
  count += 1
  total = 0
  average = 0
  moves = 0
  stock_num = int(input())
  if stock_num == 0:
    break

  stock = input().split()

  for i in stock:
    total += int(i)
  average = total/len(stock)

  for i in stock:
    moves += abs(int(i)-average)

  print("Set #" + str(count))
  print("The minimum number of moves is " + str(int(moves/2))+".")

# Box of Bricks - 2
  
k = 1
while True:
    a = 0
    n = int(input())
    m = 0
    if n == 0:
        exit(0)
    h = input().split(' ')
    for i in range(n):
        a += int(h[i])
    b = int(a/n)
    for i in range(n):
        if int(h[i]) != b:
            m += abs(int(h[i]) - b)
    print("Set #{}".format(k))
    print("The minimum number of moves is {}.".format(int(m/2)))
    k += 1
