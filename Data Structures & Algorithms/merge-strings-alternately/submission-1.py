class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = 0
        idx2 = 0
        new = []
        while idx1 < len(word1) or idx2 < len(word2):
            new.append(word1[idx1] + word2[idx2])
            idx1 += 1
            idx2 += 1
            if idx1 == len(word1):
                new.append(word2[idx2:])
                break
            if idx2 == len(word2):
                new.append(word1[idx1:])
                break
        new = "".join(new)
        return new