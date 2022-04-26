# g448 印出 A 到 Z ，a到z，及它們的 ASCII 碼值

print("A 65 a 97\nB 66 b 98\nC 67 c 99\nD 68 d 100\nE 69 e 101\nF 70 f 102\nG 71 g 103\nH 72 h 104\nI 73 i 105\nJ 74 j 106\nK 75 k 107\nL 76 l 108\nM 77 m 109\nN 78 n 110\nO 79 o 111\nP 80 p 112\nQ 81 q 113\nR 82 r 114\nS 83 s 115\nT 84 t 116\nU 85 u 117\nV 86 v 118\nW 87 w 119\nX 88 x 120\nY 89 y 121\nZ 90 z 122")

# g562: 你說的是甚麼?

a = input().split()
del a[0]
print(a[int(a[-1])-1])

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
