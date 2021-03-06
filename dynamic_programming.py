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

# dp 
def how_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    memo[target_sum] = combination + [num]
                    return memo[target_sum]
        memo[target_sum] = None
        return memo[target_sum]

    return helper(target_sum, numbers)
################################################################################################

# best sum, same as above but with smallest array

## Brute-Force
def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        if remainder >= 0:
            combination = best_sum(remainder, numbers)
            if combination is not None:
                combination = combination + [num]
                if shortest_combination is None or len(combination) < len(
                    shortest_combination
                ):
                    shortest_combination = combination
    return shortest_combination


## DP

def best_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(
                        shortest_combination
                    ):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return helper(target_sum, numbers)

######################################################################################

# try to see if can make target word from word bank

def canConstruct(target, words): 
    if target == '': return True

    for word in words:
        if target.startswith(word):
            remainder = target[len(word):]
            if canConstruct(remainder, words): return True

    return False
    
print(canConstruct('red', ['re', 'd']))
print(canConstruct('reds', ['re', 'd']))

#  DP  memoization

def canConstruct(target, words, memo={}): 
    if target == '': return True
    if target in memo: return memo[target]

    for word in words:
        if target.startswith(word):
            remainder = target[len(word):]
            
            if canConstruct(remainder, words, memo):
                memo[target] = True
                return True
            
    memo[target] = False
    return False
    
    
    
print(canConstruct('red', ['re', 'd']))
print(canConstruct('reds', ['re', 'd']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeef', ['e', 'e', 'e', 'e', 'e', 'e', 'f']))

#################################################################################

def count_construct(target, word_bank):
    if target == '': return 1
    total = 0
    
    for word in word_bank:
        if target.startswith(word):
            remainder = target[len(word):]
            num_ways = count_construct(remainder, word_bank)
            total += num_ways
        
    return total
    
print(count_construct('red', ['re', 'd']))
print(count_construct('reds', ['re', 'd']))

## no with DP , memoization

def count_construct(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if target == '': return 1
    total = 0
    
    for word in word_bank:
        if target.startswith(word):
            remainder = target[len(word):]
            num_ways = count_construct(remainder, word_bank, memo)
            total += num_ways
        
    memo[target] = total
    return total
    
print(count_construct('red', ['re', 'd']))
print(count_construct('reds', ['re', 'd']))