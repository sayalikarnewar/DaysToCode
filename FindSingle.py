#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 

def singleNumber(nums) -> int:
        i=0
        n = len(nums)
        while i<n:
            if nums.count(nums[i])==1:
                return (nums[i])
                break
            i+=1    
            
singleNumber([4,1,2,1,2])   


 '''
    Input: [4,1,2,1,2]
    Output: 4
    '''
