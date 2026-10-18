class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numap = {}
        for num in nums:
            if num in numap:
                numap[num] = numap[num] + 1
            else:
                numap[num] = 1
        
        sorted_keys = sorted(numap, key=numap.get, reverse=True)
        out = []
        for i in range(k):
            out.append(sorted_keys[i])

        return out