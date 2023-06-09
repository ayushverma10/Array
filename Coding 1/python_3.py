#Four sum

def foursums(nums,target):
    nums.sort()
    result=[]

    for i in range(len,nums):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                  if nums[i]+nums[j]+nums[k]+nums[l] == target:
                    Quadruplet=list([nums[i],nums[j],nums[k],nums[l]])
                result.append(Quadruplet) 
    print(result)