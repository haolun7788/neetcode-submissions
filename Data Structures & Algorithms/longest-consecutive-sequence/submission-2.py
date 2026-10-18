class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        for n in nums:
            hmap[n] = 1
        curmax = 0

        cur = 1
        for n in hmap:
            if n - 1 not in hmap:
                cur = 1
                while n + cur in hmap:
                    cur += 1
                curmax = max(curmax, cur)

        return curmax
        