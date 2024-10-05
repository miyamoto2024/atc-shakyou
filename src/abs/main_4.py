# NOTE: https://atcoder.jp/contests/abs/tasks/abc088_b

N = int(input())
S = list(map(int, input().split()))
S.sort()

alice = 0
bob   = 0

flag = True
for i in range(N):
  if (flag == True):
    alice += S[len(S) - 1 - i]
    flag = False
  else:
    bob += S[len(S) - 1 - i]
    flag = True

print(alice - bob)
