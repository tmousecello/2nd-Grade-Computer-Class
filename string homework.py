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
