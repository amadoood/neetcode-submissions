class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}
        for st in strs:
            freqArray = [0] * 26
            for c in st:
                freqArray[ord(c) - ord('a')] += 1
            hashableFreqArray = tuple(freqArray)
            if anagramGroups.get(hashableFreqArray):
                anagramGroups[hashableFreqArray].append(st)
            else:
                anagramGroups[hashableFreqArray] = [st]
            
        return list(anagramGroups.values())