# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))

# dp初期化（第一添字がカードi、第二添字が合計値）
dp = [[0] * (S+1) for i in range(N+1)]

# カード0枚は合計値0
dp[0][0] = True
for i in range(1, S+1):
    dp[0][i] = False

# 条件A「dp[i-1][j]」：カードi-1の時点で合計jであり、カードiを選ばない ならば dp[i][j]はTrue
# 条件B「dp[i-1][j-A[i]]」：カードi-1の時点で合計j-Aiであり、カードiを選ぶ ならば dp[i][j]はTrue
for i in range(1, N+1):
    for j in range(S+1):
        # 合計値jがA[i]よりも小さかったら条件Aのみを見る
        # 都合上Aからiからマイナス1して計算
        if (j < A[i-1]):
            if (dp[i-1][j]):
                dp[i][j] = True
            else:
                dp[i][j] = False
        if (j >= A[i-1]):
            if (dp[i-1][j] or dp[i-1][j-A[i-1]]):
                dp[i][j] = True
            else:
                dp[i][j] = False
if (dp[N][S]):
    print('Yes')
else:
    print('No')
