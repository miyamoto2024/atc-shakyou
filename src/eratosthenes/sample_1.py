# 2から入力値Nまでの素数を列挙するプログラム
# 2 < N <= 10**9

N = int(input())
isPrimes = []
primes = [2] # 「2」は素数確定

# 2k+1のみ対象とし、全て素数であると仮定
for i in range(3, N+1, 2):
    isPrimes.append(True)

d = 3
for index, isPrime in enumerate(isPrimes):
    if(isPrime == True):
        primes.append(d)
        t = d*d
        x = index+1
        for j in range(t, N+1, d*2):
            isPrimes[j - (j-(d*x))+index] = False
            x += 1
    d += 2

print(primes)