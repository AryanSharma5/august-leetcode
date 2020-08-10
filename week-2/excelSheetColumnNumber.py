class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        count = len(s)-1
        i=0
        while count>=0:
            ans += (ord(s[i]) - ord('A') + 1)*(26**(count))
            i+=1
            count-=1
        return ans