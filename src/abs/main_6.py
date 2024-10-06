# NOTE: https://atcoder.jp/contests/abs/tasks/arc065_a
# この順でreplaceすれば被ることなく消せるという。。

str = input()

str = str.replace('eraser', '')
str = str.replace('erase', '')
str = str.replace('dreamer', '')
str = str.replace('dream', '')

if (len(str) == 0):
  print("YES")
else:
  print("NO")
