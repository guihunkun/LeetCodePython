class Solution:
    def palindrome(self,s,i,j):
        return all(s[k] == s[j-k+i] for k in range(i, j))
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i]!=s[len(s)-1-i]:
                j=len(s)-1-i
                return self.palindrome(s,i+1,j) or self.palindrome(s,i,j-1)
        return True
