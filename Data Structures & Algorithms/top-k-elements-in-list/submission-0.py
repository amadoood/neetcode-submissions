class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        numsCounter = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            numsCounter[num] = 1 + numsCounter.get(num, 0)
        
        for key,value in numsCounter.items():
            buckets[value].append(key)
        
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result