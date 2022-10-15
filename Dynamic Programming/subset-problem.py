def subSum(arr,target):
    n = len(arr)
    dp = [[None]*(target+1) for _ in range(n+1)]

    # Initialise DP array !!
    # If no. of elements in arr are 0 then Target sum is not possible
    # Target sum = 0 is always possible i.e, by keeping the array subset as null/phi.
    for i in range(target+1):
        dp[0][i] = False
    for j in range(n+1):
        dp[j][0] = True

    # An element can be chosen only if sum is less han arr[i] else it cannot be included
    for i in range(1,n+1):
        for j in range(target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # Return last cell as it contains answer
    return dp[n][target]

def isPossible(arr):
    # If arr has sum P and two subsets have same sum S respectively then S+S =P. Therefore we need to find
    # subset of sum P//2 and other subset will have same sum.
    P = sum(arr)
    S = P // 2
    # ReturnTrue if subset exists else False
    return(subSum(arr,S))

if __name__ == '__main__':
    arr = [3, 1, 1, 2, 2, 1]
    # An array can be divided into two equal halves only if sum of arr is even else it is not possible
    if sum(arr) % 2:
        print('Equal Subset cannot be formed !!')
    else:
        boolean = isPossible(arr)
        if boolean:
            print('Equal Sum Subsets are possible !')
        else:
            print('Equal Sum Subsets are not possible !')