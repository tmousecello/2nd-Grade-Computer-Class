# g448-1: 印出 A 到 Z ，a到z，及它們的 ASCII 碼值

print("A 65 a 97\nB 66 b 98\nC 67 c 99\nD 68 d 100\nE 69 e 101\nF 70 f 102\nG 71 g 103\nH 72 h 104\nI 73 i 105\nJ 74 j 106\nK 75 k 107\nL 76 l 108\nM 77 m 109\nN 78 n 110\nO 79 o 111\nP 80 p 112\nQ 81 q 113\nR 82 r 114\nS 83 s 115\nT 84 t 116\nU 85 u 117\nV 86 v 118\nW 87 w 119\nX 88 x 120\nY 89 y 121\nZ 90 z 122")

# g448-2: 印出 A 到 Z ，a到z，及它們的 ASCII 碼值
Uc = []
Ca = []
Lc = []
La = []
for i in range(26):
    Ca.append(ord('A')+i)
    Uc.append(chr(Ca[i]))
    Lc.append(Uc[i].casefold())
    La.append(ord(Lc[i]))
    print(Uc[i], Ca[i], Lc[i], La[i], sep=" ")

# g562-1: 你說的是甚麼?

a = input().split()
del a[0]
print(a[int(a[-1])-1])

# g562-2: 你說的是甚麼?

L = input().split(" ")
i = int(L[0])
L.remove(L[0])
j = int(L[i])
print(L[j-1])

# g561: 儲存名字

print("Your name is " + input())

# g542: 只留前幾字

while True:
  try:
    a = input().split()
    b = []
    cout = ""
    for i in a[0]:
      b.append(i)
    b = b[0:int(a[1])]
    for i in b:
      cout += i
    print(cout)
  except EOFError:
    break

# g542: 只留前幾字

while True:
    try:
        L = input().split(" ")
        i = int(L[1])
        l = L[0]
        print(l[0:i])
    except Exception:
        exit(0)

# f530: GJ-b006-Hello, XXX! (**) 

print("Hello, "+input()+"!")

# f531: GJ-b007-倒背如流 (**) 

txt = input()[::-1]
print(txt)

# f532: GJ-b008-迴文 (**) 

txt = input()
txt2 = txt[::-1]
if txt == txt2:
  print("YES")
else:
  print("NO")
  
# f533-1: GJ-b009-無限猴子定理 

txt = input().split()
a,b = [],[]
count = 0
for i in txt[0]:
  a.append(i)
for i in txt[1]:
  b.append(i)

for i in a:
  if i in b:
    count+=1
    del b[0:b.index(i)+1]
    continue
  else:
    print("NO")
    break

if count == len(a):
  print("YES")

# f533-2: GJ-b009-無限猴子定理 

t = input().split()
a = list(t[0])
b = list(t[1])
for i in a:
    if i in b:
        del b[0:b.index(i)+1]
    else:
        print("NO")
        exit(0)
print("YES")

# f534: GJ-b010-編碼破解

ascii = []
out = ""
for i in input():
  ascii.append(ord(i))

for i in ascii:
  if i == 65:
    out+="Y"
  elif i == 66:
    out+="Z"
  else:
    out+=chr(int(i)-2)
print(out)

# f535-1: GJ-b011-字裡玄機 
a = []
for i in input():
  a.append(i)
b = []
for i in input():
  b.append(i)
c = []
for i in input():
  c.append(i)

num = 9
a2 = ""
b2 = ""
c2 = ""


for i in a:
  try:
    num += int(i)
    a2 += i
  except Exception:
    continue
for i in b:
  try:
    num += int(i)
    b2 += i
  except Exception:
    continue
for i in c:
  try:
    num += int(i)
    c2 += i
  except Exception:
    continue

print(int(a2)+int(b2)int(c2))

# f535-2: GJ-b011-字裡玄機

s = 0
for i in range(3):
    n = input()
    p = []
    for i in n:
        try:
            p.append(int(i))
        except Exception:
            pass
    for j in range(len(p)):
        s += p[j]*(10**(len(p)-j-1))
print(s)

# f536-1: GJ-b012-羅馬數字 

r = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

s = input()
a = [i for i in s]


res = 0
for i in a:
  res += r[i]

for i in range(0,len(a)-1,1):
  if r[a[i]] < r[a[i+1]]:
    res -= 2*r[a[i]]

print(res)

# f536-2: GJ-b012-羅馬數字 

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
num = 0
r = input()
for i in range(len(r)):
    if i+1 < len(r) and roman[r[i]] < roman[r[i+1]]:
        num -= roman[r[i]]
    else:
        num += roman[r[i]]
print(num)

# d235: 10929 - You can say 11

while True:
  r = str(input())
  if r == "0":
    break
  else:
    num = [int(i) for i in r]
    a = sum(num[0::2])
    b = sum(num[1::2])
    if abs(a-b)%11 == 0:
      print(r +" is a multiple of 11.")
    else:
      print(r +" is not a multiple of 11.")

# f537: GJ-b013-評語重排 

a = input()
b = input()
c = input()
print(c,)
print(a)
print(b)

# f538: GJ-b014-打蚊子大賽 
ing1 = input().split()
g1 = []
for i in ing1:
  g1.append(int(i))
ing2 = input().split()
g2 = []
for i in ing2:
  g2.append(int(i))
ing3 = input().split()
g3 = []
for i in ing3:
  g3.append(int(i))

if sum(g1)>sum(g2) and sum(g1)>sum(g3):
  print("1",str(sum(g1)))
elif sum(g2)>sum(g3) and sum(g2)>sum(g1):
  print("2",str(sum(g2)))
else:
  print("3",str(sum(g3)))

# f539: GJ-b015-追殺比爾 
line1 = input().split()
line2 = input().split()
line3 = input().split()

if "BILL" in line1:
  print("1", str(int(line1.index("BILL"))+1))
elif "BILL" in line2:
  print("2", str(int(line2.index("BILL"))+1))
elif "BILL" in line3:
  print("3", str(int(line3.index("BILL"))+1))
else:
  print("NO")
