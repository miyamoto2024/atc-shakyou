# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
# pythonならbisect使ってもいいが自力で
N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

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
