def SingleNumber(nums):
    
    res = 0
    for num in nums:
        res ^= num
    return res
    

nums = [1,1,2,3,3]
SingleNumber(nums)