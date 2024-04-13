class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = collections.defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                freq[index] += 1


            anagramMap[tuple(freq)].append(s)

        return anagramMap.values()
        