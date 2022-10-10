def climbStairs(n):
    first = 1
    second = 1
    
    for i in range(n - 1):
        temp = first + second
        first = second
        second = temp
        
    return second