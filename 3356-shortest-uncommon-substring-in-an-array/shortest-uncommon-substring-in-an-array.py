class Solution:
    def shortestSubstrings(self, arr):
        # Using defaultdict to automatically handle missing keys
        names = arr
        trie = defaultdict(set)
        
        # Populate the trie with all possible substrings of each name
        for idx, name in enumerate(names):
            for start in range(len(name)):
                for length in range(1, len(name) - start + 1):
                    substring = name[start:start+length]
                    trie[substring].add(idx)
        
        # To emulate TreeMap's ordering by length and then lexicographically
        # sorted_trie = OrderedDict(sorted(trie.items(), key=lambda x: (len(x[0]), x[0])))

        # Dictionary to store the result
        res = [""] * len(arr)
        
        # Check each entry in the sorted trie to find the first unique substring for each name
        for substring, indices in trie.items():
            if len(indices) == 1:  # Only one index means it's unique
                name_index = indices.pop()
                
                if res[name_index] == "":
                    res[name_index] = substring
                    continue
        
                elif len(substring) == len(res[name_index]) and substring < res[name_index]:
                    res[name_index] = substring

                elif len(substring) < len(res[name_index]):
                    res[name_index] = substring

        return res

        