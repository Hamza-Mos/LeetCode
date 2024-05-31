class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.groups = collections.defaultdict(list)
        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1

            self.groups[tuple(freq)].append(s)

        return self.groups.values()
        