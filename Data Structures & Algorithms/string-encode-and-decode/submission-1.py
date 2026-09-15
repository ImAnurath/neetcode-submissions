class Solution:

    def encode(self, strs: List[str]) -> str:
        whole = ""
        for word in strs:
            whole += str(len(word)) + '/'
        strs = "".join(strs)
        whole += '#' + str(strs)
        return whole

    def decode(self, s: str) -> List[str]:
        lenghts = []
        l = ""
        st = 0
        for idx, ch in enumerate(s):
            if ch == '#':
                st = idx + 1
                break
            if ch != '/':
                l += ch
            if ch == '/':
                lenghts.append(int(l))
                l = ""
        clean = s[st:]
        decod = []
        current = 0
        for lenght in lenghts:
            decod.append(clean[current:current+lenght])
            current += lenght
        return decod
