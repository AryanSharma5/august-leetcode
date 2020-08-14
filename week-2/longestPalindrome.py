from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for freq in Counter(s).values():
            ans += (freq//2)*2
            if not ans&1 and freq&1:
                ans += 1
        return ans