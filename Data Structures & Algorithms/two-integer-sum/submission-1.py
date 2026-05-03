class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h= {}
        for i in range(len(nums)):
            a =  target - nums[i]
            if a in h: 
                return [ h[a],i]
            else:
                h[nums[i]] = i
        