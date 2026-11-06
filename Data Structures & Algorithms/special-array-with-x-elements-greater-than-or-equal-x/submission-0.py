class Solution:
    def specialArray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        L, R = 1, len(nums)
        while L <= R:
            M = (L + R) // 2
            count = sum(1 for num in nums if num >= M)
            if count == M:
                return count
            elif count < M:
                R = M - 1
            else:
                L = M + 1
        return -1
        