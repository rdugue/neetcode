class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        for a, b in zip(sorted(s), sorted(t)):
            if a != b:
                return False 

        return True 