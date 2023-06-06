class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
//both the solutions are acceptable
        for i in range(len(haystack) + 1 - len(needle)):
            #     for j in range(len(needle)):
            #         if haystack[i+j]!= needle[j]:
            #             break
            #         if j == len(needle) -1 :
            #             return i
            # return -1
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
