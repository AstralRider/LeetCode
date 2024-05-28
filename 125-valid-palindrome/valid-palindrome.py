class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()

        L = 0
        R = len(string) - 1

        while L <= R:
            if string[L] != string[R]:
                return False
            else:
                L += 1
                R -= 1
        return True