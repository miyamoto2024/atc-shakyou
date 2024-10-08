# NOTE: https://atcoder.jp/contests/abs/tasks/arc089_a
# 以下の2点が分かるかどうか。（「マンハッタン距離」を参照）
# 座標x,yから座標xi,yiに移動する際にかかる時間d = |xi - x| + |yi - y|が分かること。
# 使える時間dtとdの差が偶数だったら到着可能、奇数だったら到着不可能と分かること。

N = int(input())
T = []
X = []
Y = []

# start
T.append(0)
X.append(0)
Y.append(0)

for i in range(N):
  l = list(map(int, input().split()))
  T.append(l[0])
  X.append(l[1])
  Y.append(l[2])

flag = False
for i in range(N):
  distance = abs(X[i + 1] - X[i]) + abs(Y[i + 1] - Y[i])
  t = T[i + 1] - T[i]
  if (distance == t or t > distance and (t - distance) % 2 == 0):
    flag = True
  else:
    flag = False
    break
  
if (flag == True):
  print("Yes")
else:
  print("No")