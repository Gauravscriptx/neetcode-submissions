class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            compliement=target - num
            if compliement in seen:
                return[seen[compliement],i]
            seen[num]=i