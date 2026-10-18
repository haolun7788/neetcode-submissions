class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        curmax = 0
        hmap = {}
        while right < len(s):
            hmap[s[right]] = hmap.get(s[right], 0) + 1
            while (right - left + 1) - max(hmap.values()) > k:
                hmap[s[left]] -= 1
                left += 1
            curmax = max(right - left + 1, curmax)
            right += 1
        
        return curmax
