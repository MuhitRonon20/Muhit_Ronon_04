class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1  # Move past '#'

            # Extract the exact substring using the parsed length
            res.append(s[i : i + length])
            i += length

        return res