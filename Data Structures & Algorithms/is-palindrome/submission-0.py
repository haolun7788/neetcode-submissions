class Solution:
    def isPalindrome(self, s: str) -> bool:
        done = ""
        for c in s:
            if c.isalnum():
                done += c.lower()

        left, right = 0, len(done) - 1
        while left < right:
            if done[left] != done[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True