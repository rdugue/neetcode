class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums
        if n == 2:
            return nums if nums[0] <= nums[1] else [nums[1], nums[0]]
        
        split = n // 2
        left = self.sortArray(nums[:split])
        right = self.sortArray(nums[split:])

        m, n = len(left), len(right)
        arr1 = []
        arr2 = []
        i, j = 0, 0

        while i < m and j < n:
            if left[i] <= right[j]:
                arr1 += [left[i]]
                i += 1
            else:
                arr1 += [right[j]]
                j += 1

        if i < m:
            arr2 += left[i:]
        if j < n:
            arr2 += right[j:]

        return arr1 + arr2