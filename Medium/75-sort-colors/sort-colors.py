class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = 0

        # Count 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1

        # Fill 0s
        index = 0
        for i in range(zero):
            nums[index] = 0
            index += 1

        # Fill 1s
        for i in range(one):
            nums[index] = 1
            index += 1

        # Fill 2s
        for i in range(two):
            nums[index] = 2
            index += 1