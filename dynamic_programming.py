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

#############################################################################

#  grid traveler, 2D grid start top left, how many ways to get to bottom right

#  brute force way
def grid(m,n):
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    
    return grid(m-1, n) + grid(m, n-1)
    
print(grid(3,3))    

#  dp way
def grid(m,n, memo={}):
    key = '{}, {}'.format(m, n)
    if key in memo: return memo[key]
    
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    
    memo[key] = grid(m-1, n, memo) + grid(m, n-1, memo)
    return memo[key]
    
print(grid(10,10))  

####################################################################################

# brute force  , find out of you can hit the target from nums

def can_sum(target, nums):
    if target == 0: return True
    if target < 0: return False
    
    for num in nums:
        remainder = target - num
        if can_sum(remainder, nums) == True: return True
    
    return False

print(can_sum(7, [2, 3]))
