# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
# # forでやると...TLEで間に合わない
# for i in range(len(A)-1, 0, -1):
#     for j in range (i):
#         result = A[i] - A[j]
#         # print(f"A[i]: {A[i]}")
#         # print(f"A[j]: {A[j]}")
#         if (result <= K):
#           ans += 1

# print(ans)

# しゃくとり法でやる
R = [0] * N
for i in range(len(A)-1):
   # しゃくとりスタート地点は0から
    if (i != 0):
        R[i] = R[i-1]

    # R位置+1から現在位置を引いた値がK以下の場合、R位置を進める
    while (R[i] < len(A)-1 and A[R[i]+1]-A[i] <= K):
        # この値は、Ri位置から進んだ距離
        R[i] += 1

for i in range (len(A)-1):
    ans += R[i] - i
    # print(f"R[i]: {R[i]}, i: {i}")
print(ans)
