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
        if len(a) != len(b):
            return False 
        fa = {}
        fb = {}
        for ca, cb in zip(a, b):
            try:
                fa[ca] += 1
            except KeyError:
                fa[ca] = 1
            try:
                fb[cb] += 1
            except KeyError:
                fb[cb] = 1
        try:
            return all([fa[k] == fb[k] for k in fa.keys()])
        except:
            return False
