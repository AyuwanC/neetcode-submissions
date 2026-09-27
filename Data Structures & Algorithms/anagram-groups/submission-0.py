class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            hash_table[tuple(count)].append(word)
        return list(hash_table.values())
