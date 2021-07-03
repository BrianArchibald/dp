#  brute force for finding the fib number

def fib(n):
    if n <= 2: return 1
    
    return fib(n-1) + fib(n-2)

print(fib(7))

#  using dp and memoization

def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(60))