# Single Number 2

def SingleNumber(nums):
    result=0
    for num in nums:
     result ^=num
     return result
    
    #  Example

    nums=[4,4,5,7,7,7,6,6]
    print(nums)

    #output--5
   

     