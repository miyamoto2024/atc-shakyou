# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 秒数
ok = 10**9
ng = 0

def isOK(sec :int):
    sum = 0
    # 1秒間に1枚印刷できるプリンタについて、4秒間では4枚印刷され、
    # 2秒間に1枚印刷できるプリンタについて、4秒間では2枚印刷される
    # その合計
    for i in A:
        sum += sec // i
    if (sum >= K):
        return True
    else:
        return False

while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if (isOK(mid)):
        ok = mid
    else:
        ng = mid

print(ok)
