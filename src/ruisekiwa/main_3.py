# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
H, W = list(map(int, input().split()))
# 0マス目を含める
T = [[0] * (W+1) for _ in range(H+1)]
S = [[0] * (W+1) for _ in range(H+1)]
for i in range(1, H+1):
    X = list(map(int, input().split()))
    for j in range(1, W+1):
        T[i][j] = X[j-1]
        
# 横
for i in range(1, H+1):
    for j in range(1, W+1):
        S[i][j] = S[i][j-1]+T[i][j]
        
# 縦
for j in range(1, W+1):
    for i in range(1, H+1):
        S[i][j] = S[i-1][j] + S[i][j]

Q = int(input())

for _ in range(Q):
    A, B, C, D = list(map(int, input().split()))
    print(S[C][D]+S[A-1][B-1]-S[A-1][D]-S[C][B-1])
