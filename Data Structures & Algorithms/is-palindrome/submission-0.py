class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for char in s:
            if char.isalnum():
                newS += char.lower()

        return newS == newS[::-1]


        