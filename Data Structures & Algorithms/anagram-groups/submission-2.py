from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in res:
                res[sorted_s] = []
            
            res[sorted_s].append(s)

        return list(res.values())



       


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)

#         for s in strs:
#             sorted_s = "".join(sorted(s))
#             res[sorted_s].append(s)
        
#         return list(res.values())