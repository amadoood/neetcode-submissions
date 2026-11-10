class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        L, R = 0, len(s_lower)-1
        while L < R:
            while L < R and s_lower[L].isalnum() is False:
                L+=1
            while L < R and s_lower[R].isalnum() is False:
                R-=1
            if s_lower[L] != s_lower[R]:
                return False
            L+=1
            R-=1
        return True
        