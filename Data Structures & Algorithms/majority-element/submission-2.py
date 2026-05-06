class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for n in nums:
            if n in counts.keys():
                counts[n] += 1
                if counts[n] > len(nums) / 2:
                    return n
            else:
                counts[n] = 1

        return nums[0]