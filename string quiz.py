# a499: 愛附中大點名

while True:
  try:
    name = input()
    print(name, "Love HSNU forever!")
  except EOFError:
    break
    
# f720: GJ-c030-5.挑戰魔王

attack = input()
hit = 0
count = 0
atk = []

for i in attack:
  atk.append(i)

for i in range(len(atk)-1):
  if atk[i] == "A" and atk[i+1] == "C":
    hit += 1

print(hit)

# f794: 數字倒轉-2

while True:
  try:
    txt = input()[::-1]
    print(int(txt))
  except EOFError:
    break
    
# g692: 每行有幾個單字

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z"
      "A","B","C","D","E","F","G","H","I","J","J","L","M",
      "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
  try:
    txt = input()
    txt_ls = [i for i in txt]
    a = 1
    for i in range(len(txt)-1):
      if txt_ls[i] not in letter and txt_ls[i+1] in letter:
        a += 1
    print(a)
  except EOFError:
    break
    
# f718: GJ-c019-6.循環字串
b = input()
a = [i for i in b]
k = 0
k_list = []

for i in range(len(a)-3):
  if a[i] == a[i+3]:
    if len(a) < 6:
      k = 0
      break
    k = 3
  else:
    k = 0
    break
if k == 3:
  k_list.append(3)

for i in range(len(a)-4):
  if a[i] == a[i+4]:
    if len(a) < 8:
      k = 0
      break
    k = 4
  else:
    k = 0
    break
if k == 4:
  k_list.append(4)

for i in range(len(a)-5):
  if a[i] == a[i+5]:
    if len(a) < 10:
      k = 0
      break
    k = 5
  else:
    k = 0
    break
if k == 5:
  k_list.append(5)

for i in range(len(a)-6):
  if a[i] == a[i+6]:
    if len(a) < 12:
      k = 0
      break
    k = 6
  else:
    k = 0
    break
if k == 6:
  k_list.append(6)

if k_list == []:
  print(0)
else:
  print(min(k_list))

r = {
    'W' : "Q",
    'E' : "W",
    'R' : "E",
    'T' : "R",
    'Y' : "T",
     'U' : "Y",
     'I' : "U",
     'O' : "I",
     'P' : "O",
     '[' : "P",
     'S' : "A",
     'D' : "S",
     'F' : "D",
     'G' : "F",
     'H' : "G",
     'J' : "H",
     'K' : "J",
     'L' : "K",
     ';' : "L",
     '\\' : "]", 
     ']' : "[",
     'X' : "Z",
     'C' : "X",
     'V' : "C",
     'B' : "V",
     'N' : "B",
     'M' : "N",
     ',' : "M",
     '.' : ",",
     '/' : ".",
     '1' : "`",
     '2' : "1",
     '3' : "2",
     '4' : "3",
     '5' : "4",
     '6' : "5",
     '7' : "6",
     '8' : "7",
     '9' : "8",
     '0' : "9",
     '-' : "0",
     '=' : "-",
     ' ' : ' ',
     '\'' : ";"
}


while True:
  try:
    txt = input()
    cout = ""
    for i in txt:
      cout += r[i]
    print(cout)
  except EOFError:
    break
