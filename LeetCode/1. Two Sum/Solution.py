class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        
        for i in range(len(nums)):
            t= target-nums[i]
            if(t in nums and t in d.keys()):
                return [i,d[t]] 
            else:
                d[nums[i]] = i