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

#  using dp and memoization, the key in memo is the target as the nums don't change, you can resuse them.
def can_sum(target, nums, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    
    for num in nums:
        remainder = target - num
        if can_sum(remainder, nums, memo) == True:
            memo[target] = True
            return True
            
    memo[target] = False
    return False
    
print(can_sum(300, [7, 14]))  

#########################################################################################################
# how sum, return any array that can equal sum of the target

#  brute force method

def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = how_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                return combination
    return None
    
print(how_sum(7, [2, 3]))