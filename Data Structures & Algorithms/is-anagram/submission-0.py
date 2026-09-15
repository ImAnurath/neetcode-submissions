class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            def freq(arr):
                ht = {}
                for ele in arr:
                    if ele in ht:
                        ht[ele] += 1
                    else:
                        ht[ele] = 1
                return ht
            hts = freq(s)
            htt = freq(t)
            return freq(s) == freq(t)