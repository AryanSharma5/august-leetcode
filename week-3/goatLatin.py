class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split()
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(s)):
            if s[i][0].lower() in vowels:
                s[i] += 'ma'
            else:
                s[i] = s[i][1:] + s[i][0] + 'ma'
            s[i] += 'a'*(i+1)
        return ' '.join(s)