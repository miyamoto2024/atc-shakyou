# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
import itertools
D = int(input())
N = int(input())
T = [0] * (D+2)
for _ in range(N):
    L, R = list(map(int, input().split()))
    T[L] += 1
    T[R+1] -= 1
S = list(itertools.accumulate(T))
for i in range(1, D+1):
    print(S[i])
