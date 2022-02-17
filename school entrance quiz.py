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

#d067

i = input()
if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
    print("a leap year")
else:
    print("a normal year")

#d069

k = int(input())
for j in range(k):
    i = int(input())
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")
#d070

while True:
    i = int(input())
    if i == 0:
        break
    elif ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")

#d071

while True:
    try:
        i = int(input())
    except Exception: # I'm lazy. So?
        break
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")

#d072

k = int(input())
for j in range(k):
    i = int(input())
    if ((int(i) % 4 == 0) and (int(i) % 100 != 0)) or (int(i) % 400 == 0):
        print("Case {}: a leap year".format(j+1))
    else:
        print("Case {}: a normal year".format(j+1))

#a943

for i in range (1,8):
    for j in range (1,8):
        print("{}*{}={}\t".format(i,j,i*j), end='')
    print('\n')

#f220

n = int(input())
for i in range (1,n+1):
        print("{}".format(i)*i)

#f221

n = int(input())
for i in range (1,n+1):
        print("_"*(n-i),end='')
        print("{}".format(i)*(2*i-1))

#f218

n = int(input())
sqrtn = int(n**0.5)
if n >1:
    for i in range (2,sqrtn+1):
        if n % i == 0:
            print("NO")
            exit(0)
print("YES")

#f216

num = input().split(' ')
a = int(num[0])
b = int(num[1])
def gcd(c, d):
    if c+d != c or d:
        return gcd(d, c%d)
    else:
        print(c+d)
gcd(a,b)

#b138

h = input().split(' ')
l = int(input())
n = 0
for i in range(10):
    a = int(h[i])
    if a <= l + 30:
        n += 1
print(n)

#c067

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
