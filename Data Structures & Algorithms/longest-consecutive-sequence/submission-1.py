class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsSet = set(nums)
        '''
        currentMin = float('inf')
        resultCount, currentCount = 0, 0
        while numsSet:
            for num in numsSet:
                if num < currentMin:
                    currentMin = num
            while currentMin in numsSet:
                currentCount = currentCount + 1
                numsSet.remove(currentMin)
                currentMin = currentMin + 1
            if currentCount > resultCount:
                resultCount = currentCount
            currentCount = 0
            currentMin = float('inf')
        return resultCount
        '''
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