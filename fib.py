dp = [0, 1]
def fib(n):
    if n < 0:
        print('error: invalid index')
    elif n <= len(dp):
        return dp[n - 1]
    else:
        tmp = fib(n - 1) + fib(n - 2)
        dp.append(tmp)
        return tmp

n = int(input())

for i in range(n):
    if i == n - 1:
        print(fib(i))
        continue;
    
    print(fib(i), end=' ')
