# NOTE: https://atcoder.jp/contests/abc014/tasks/abc014_2
# 全探索ではなく、bit探索でやってみた。

product_count, target = map(int, input().split())
products_price = input().split()
total_price = 0

bit = bin(target)[2:]

for i in range(len(bit)):
  if (target & 1 << i):
    total_price += int(products_price[i])

print(total_price)

