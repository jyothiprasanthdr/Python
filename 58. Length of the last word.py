class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=s.strip()

        # words = s.split()  Here the TC ans SC is O(n)
        # return len(words[-1])

        # But here SC is O(1)
        length, counter = len(s), 0
        while length > 0:
            length -= 1
            if s[length] != " ":
                counter += 1
            elif counter > 0:
                return counter
        return counter
