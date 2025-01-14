# [NOTE] https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp初期化
dp = [0] * (N+10)
# 初めは1番目の部屋から始まり、1番目の部屋に行くのは0分
dp[1] = 0
# 一番目の部屋から2番目の部屋に行くのは2分
dp[2] = A[0]

for i in range(3, N+1):
    # インデックスに注意
    a = dp[i-1]+A[i-2]
    b = dp[i-2]+B[i-3]
    dp[i] = min(a, b)

print(dp[N])
