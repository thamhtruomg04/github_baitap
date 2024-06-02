class Solution:
    def isValid(self, s: str):
        for i in range(len(s)):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return s == ''

sol = Solution()
print(sol.isValid("()"))