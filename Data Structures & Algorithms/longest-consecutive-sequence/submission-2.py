class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsSet = set(nums)
        maxCount, currentCount = 0, 1
        for num in numsSet:
            if num - 1 not in numsSet:
                current = num
                while current + 1 in numsSet:
                    currentCount = currentCount + 1
                    current = current + 1
                if currentCount > maxCount:
                    maxCount = currentCount
                currentCount = 1
        return maxCount