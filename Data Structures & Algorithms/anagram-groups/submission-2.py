class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for s in strs:
            if len(output) == 0:
                output += [[s]]
            else:
                found = False
                for group in output:
                    found = self._isAnagram(group[0], s)
                    if found:
                        group += [s]
                        break
                if not found:
                    output += [[s]]
        return output 

        
    def _isAnagram(self, a: str, b: str) -> bool:
        return sorted(a) == sorted(b)
