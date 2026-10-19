class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_map = {}
        for i in paths:
            hash_map[i[0]] = i[1]
        print(hash_map)
        for i in hash_map:            
            if hash_map[i] not in hash_map:
                return hash_map[i]
