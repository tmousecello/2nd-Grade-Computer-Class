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

# 閏年判斷

year = int(input())
if year % 4 == 0 and year % 100 != 0:
  print("YES")
elif year % 4 == 0 and year % 100 == 0 and year % 400==0:
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
    
# 3N+1

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
    
# 所有位數和

num = input()
sum = int(0)
for i in num:
  sum += int(i)
print(sum)

# 一千遍我愛你

for i in range(int(input())):
  print("I love you.")
  
# 倒數計時

c = ""
for i in range(int(input()), -1, -1):
  c += str(i)
  c += " "
print(c)

# P(N,R)
# 本題解法邪教

a = input().split()
num1 = a[0]
num2 = a[1]
sum = ""

for i in range(int(num2)):
  sum += str(int(a[0])-int(i))
  sum += "*"

sum = sum.rstrip("*")
print(eval(sum))

# 連續整數相加

5a = input().split()
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

