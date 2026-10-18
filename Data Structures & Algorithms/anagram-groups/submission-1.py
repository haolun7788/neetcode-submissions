class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        out = []
        for s in strs:
            srt = "".join(sorted(s))
            hmap[srt].append(s)      

        return list(hmap.values())