class Solution:

    def encode(self, strs: List[str]) -> str:
        solution_arr = []
        for str in strs:
            solution_arr.append(f'{len(str)}|{str}')
        return ''.join(solution_arr)

    def decode(self, s: str) -> List[str]:
        solution_arr = []
        length = ''
        append_flag = 0

        for i, char in enumerate(s):
            if append_flag != 0:
                append_flag -= 1
                continue

            if char.isdigit():
                length += char

            if char == '|':
                append_flag = int(length)
                solution_arr.append(s[i+1:i+1+int(length)])
                length = ''
        
        return solution_arr
