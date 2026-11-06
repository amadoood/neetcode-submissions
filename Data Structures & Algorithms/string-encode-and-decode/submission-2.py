class Solution:

    def encode(self, strs: List[str]) -> str:
        solution_string = ""
        for s in strs:
            solution_string += str(len(s)) + '|' + s
        return solution_string
    
    def decode(self, s: str) -> List[str]:
        solution_arr = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
            length = int(s[i:j])
            solution_arr.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return solution_arr
