class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, freq in counts.items():
            buckets[freq].append(key)

        top = []
        for i in reversed(range(len(buckets))):
            for n in buckets[i]:
                top.append(n)
                if len(top) == k:
                    return top