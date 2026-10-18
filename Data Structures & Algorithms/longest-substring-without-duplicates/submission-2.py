class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        curmax = 0
        hset = set()

        while right < len(s):
            while s[right] in hset:
                hset.remove(s[left])
                left += 1
            hset.add(s[right])
            curmax = max(right - left + 1, curmax)
            
            right += 1

        return curmax