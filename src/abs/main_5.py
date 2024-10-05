# NOTE: https://atcoder.jp/contests/abs/tasks/abc085_b
# 貪欲法で。

N = int(input())
S = []
for i in range(N):
  S.append(int(input()))
S.sort()

count = 0
now = 0
for value in S:
  if (value > now):
    now = value
    count += 1

print(count)

# NOTE: set関数でもいける。
# N = int(input())
# S = []
# for i in range(N):
#   S.append(int(input()))

# S = set(S)

# print(len(S))