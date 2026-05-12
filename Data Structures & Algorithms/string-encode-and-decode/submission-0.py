class Solution:
    def __init__(self) -> None:
        self.hash = None
        self.divisor = None

    def encode(self, strs: List[str]) -> str:
        out = ""
        self.divisor = len(strs)
        self.hash = {i: None for i in range(self.divisor)}
        for i, char in enumerate(strs):
            self.hash[i] = char
            out += char + "-"
        return out 

    def decode(self, s: str) -> List[str]:
        out = ["" for _ in range(self.divisor)]
        for i in range(self.divisor):
            out[i] = self.hash[i]
        return out