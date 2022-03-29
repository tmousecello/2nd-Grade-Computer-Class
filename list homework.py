# f589翻轉數字

a = input()
ls = a.split()
ls.reverse()
out = ""
for i in ls:
  out = out + i + " "
print(out)

# f590非波那契數列

n = [0,1,1]
count = 0
while count <= 60:
  n.append(n[-1]+n[-2]+n[-3])
  count+=1

while True:
  a = int(input())
  if a != -1:
    print(n[a])
  else:
    break
    
# f526: GJ-b002-找最大值

b = input().split()
del b[0]
if len(b) == 10:
  print("10 1000")
else:
  output1 = str(max(b))
  output2 = str(int(b.index(output1))+1)
  print(output2 + " " + output1)
 
# f527: GJ-b003-資料分組

b = input().split()
del b[0]
standard = int(b[-1])

output1 = 0
output2 = 0
for i in b:
  if int(i) > standard:
    output1 += 1
  elif int(i) < standard:
    output2 += 1
print(str(output1) + " " + str(output2))

# f592: 統一發票對獎

lottery_ticket = input().split()

while True:
  num = int(input())
  if num == -1:
    break
  else:
    if str(num) in lottery_ticket:
      print("congratulations")
    else:
      print("miss it")

# f593: 今彩539

lottery_ticket = input().split()
buy = input().split()
count = 0

for i in buy:
  if i in lottery_ticket:
    count += 1
if count != 0:
  print("Wow, you match " + str(count) + " numbers!")
else:
  print("Uh…, working hard should be a better way of making money.")

# f594: 計票系統

vege, beef, pork, chick, sea = 0,0,0,0,0

vote = input().split()
del vote[0]
for i in vote:
  if i == "0":
    vege += 1
  elif i == "1":
    beef += 1
  elif i == "2":
    pork += 1
  elif i == "3":
    chick += 1
  elif i == "4":
    sea += 1

print(str(vege)+" "+str(beef)+" "+str(pork)+" "+str(chick)+" "+str(sea))

# f528: 一個都不能少

a = input().split()
people = [str(i) for i in range(1,int(int(a[0]))+1)]
out = []
out2 = []
a.pop(0)
a.pop(0)

for i in people:
  if i in a:
    continue
  else:
    out.append(i)

for i in out:
  out2.append(int(i))

out = ""

for i in out2:
  out += str(i)
  out += " "

print(out.lstrip())

# f529: 熱門點播
max = 0

a = input().split()
a.pop(0)

for i in a:
  if a.count(i) > max:
    max = a.count(i)
    song = i

print(song+" "+str(max))

