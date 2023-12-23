class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""

        length = -1

        if(len(s) == 0):
            return 0
        elif len(s) == 1:
            return 1
        for i in list(s):
            cur = "".join(i)

            if(cur in temp):
                temp = temp[temp.index( i )+1:]
            temp= temp+"".join(i)
            length = max(len(temp), length)
        return length



        