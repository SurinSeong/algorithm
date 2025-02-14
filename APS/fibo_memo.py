# 피보나치 수열
# memoization 이용
def fibo1(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-1)
    return memo[n]


# DP 이용
def fibo2(n):
    f = [0] * (n+1)

    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]


n = 10
cnt = 0
memo = [0] * 10
