# NOTE: https://atcoder.jp/contests/abs/tasks/abc081_b
# 愚直にやるとこれ。

N = input()
S = list(map(int, input().split()))

def main(S:list) -> int:
  # validation
  for v in S:
    if v % 2 == 1 or v == 0:
      return 0
  # calc
  count = 0
  flag = True
  while flag == True:
    for i,v in enumerate(S):
      if (v % 2 == 0):
        S[i] = v // 2
      else:
        flag = False
        break
    if flag == True:
      count += 1
  return count
  
print(main(S))
