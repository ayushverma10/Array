# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same.

 
def threesum(nums):
    nums.sort()
    result=set()

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len,nums):

                if nums[i]+nums[j]+nums[k] == 0:
                    triplet=(nums [i], nums [j], nums [k])
                    result.add(triplet)

                    results=list(result)
                    print (results)
