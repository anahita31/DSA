class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Check if this sum is closer
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact answer
                if total == target:
                    return total

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return closest