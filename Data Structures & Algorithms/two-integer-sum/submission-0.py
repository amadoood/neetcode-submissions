class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            numsMap[num] = i

        for i, num in enumerate(nums):
            if target - num in numsMap and numsMap.get(target - num, -1) is not i:
                return [i, numsMap[target - num]]