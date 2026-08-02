class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        seen = set(nums)

        for i in range(1, len(nums)+1):
            if i not in seen:
                result.append(i)

        return result



        