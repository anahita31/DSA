class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range (len(nums)):
            current = nums[i]
            need = target - current 

            if need in seen:
                return[seen[need],i]
            seen[current] = i
