class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in range(len(word)):
            if 'A' <= word[i] <= 'Z':
                count += 1
        if (count == 0) or (count == len(word)) or ((count == 1) and 'A' <= word[0] <= 'Z'):
            return True
        return False