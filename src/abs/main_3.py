# NOTE: https://atcoder.jp/contests/abs/tasks/abc083_b


N, A, B = map(int, input().split())
S = []
T = []

for i in range(1, N+1):
  S.append(i)

for v in S:
  v = str(v)
  digit = len(str(v))
  num = 0
  for i in range(digit):
    num += int(v[i])
  if (A <= num and num <= B):
    T.append(int(v))

print(sum(T))
