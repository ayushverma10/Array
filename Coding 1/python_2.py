#Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    # Use two pointers approach
    i = 0  
    j = 1  
    
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    
    return i + 1
