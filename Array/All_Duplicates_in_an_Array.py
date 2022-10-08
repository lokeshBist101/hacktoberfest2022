def findDuplicates(nums):
    output = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            output.append(index + 1)
        
        nums[index] = - nums[index]
            
    return 