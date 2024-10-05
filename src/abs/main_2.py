# NOTE: https://atcoder.jp/contests/abs/tasks/abc087_b

coin500_amount = int(input())
coin100_amount = int(input())
coin50_amount  = int(input())
total_price    = int(input())

count = 0
for i in range(coin500_amount + 1):
  for j in range(coin100_amount + 1):
    for k in range(coin50_amount + 1):
      if i * 500 + j * 100 + k * 50 == total_price:
        count += 1
print(count)
