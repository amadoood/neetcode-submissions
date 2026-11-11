class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = nums[i] + nums[L] + nums[R]
                if threeSum == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                elif threeSum < 0:
                    L += 1
                else:
                    R -= 1
        return result