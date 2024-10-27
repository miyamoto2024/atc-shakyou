N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

# 通常の二分探索
# 欲しい値を効率よく求めるだけ
# ------------------------------
start = 0
end = N
ans = -1
while (start <= end):
    mid = (start + end) // 2
    if (A[mid] == X):
        ans = mid
        break
    if (A[mid] > X):
        end = mid - 1
    if (A[mid] < X):
        start = mid + 1

# 添字考慮
print(ans+1)
# ------------------------------

# めぐる式二分探索
# 条件を満たすOKエリア（左端から）と満たさないNGエリア（右端から）を狭めていくイメージ
# 境界を求めるロジックで有用
# ------------------------------
# [0]、[N]が条件を満たすパターンもあるので、インクリメント・デクリメントでスタートする
ok = N+1
ng = -1

# OKエリアを進めていいかどうかをチェックする
def isOK(i :int):
    if (A[i] >= X):
        return True
    else:
        return False

# OKエリアとNGエリアが隣り合わせになるまで続ける
while (abs(ok - ng > 1)):
    mid = (ok + ng) // 2
    if (isOK(mid)):
        ok = mid
    else:
        ng = mid

# 添字考慮
print(f"ok: {ok+1}, ng: {ng+1}")        
# ------------------------------
