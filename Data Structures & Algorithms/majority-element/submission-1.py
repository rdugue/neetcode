class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for n in nums:
            try:
                counts[n] += 1
                if counts[n] > len(nums) / 2:
                    return n
            except KeyError:
                counts[n] = 1

        return nums[0]