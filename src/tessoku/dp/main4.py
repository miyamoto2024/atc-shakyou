# [NOTE] https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s
N, W = list(map(int, input().split()))

# 品物の重さと価値を初期化
w = [0] * 109
v = [0] * 109
for i in range(1, N+1):
    w[i], v[i] = list(map(int, input().split()))

# dp初期化
dp = [[0] * (W+1) for i in range(N+1)]
dp[0][0] = 0
# 条件を見て計算に影響がない最小値で初期化
for i in range(1, W+1):
    dp[0][i] = -10 ** 10

# 条件A「dp[i-1][j]」：品物i-1の時点で合計jであり、品物iを選ばない ならば dp[i][j]はdp[i-1][j]
# 条件B「dp[i-1][j-w[i]]」：品物i-1の時点で合計j-wiであり、品物iを選ぶ ならば dp[i][j]はdp[i-1][j-wi]+vi
for i in range(1, N+1):
    for j in range(W+1):
        # 合計値jがw[i]よりも小さかったら条件Aのみを見る
        if (j < w[i]):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

# 配列から最大値を求める（dp[N][i]から最大を探す）
ans = 0
for i in range(W+1):
    ans = max(ans, dp[N][i])
print(ans)
