# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
import itertools
N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
# 0日目は0人
T = [0]
T += list(itertools.accumulate(A))
for _ in range (Q):
    X = list(map(int, input().split()))
    print(T[X[1]] - T[X[0]-1])
