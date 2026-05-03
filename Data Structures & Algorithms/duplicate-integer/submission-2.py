class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=list()*len(nums)
        for i in range(len(nums)):
            if nums[i] in a:
                return True 
            else:
                a.append(nums[i])
            i+=1
        return False
