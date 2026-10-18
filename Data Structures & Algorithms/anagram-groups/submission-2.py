class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        out = []
        for s in strs:
            srt = "".join(sorted(s))
            hmap.setdefault(srt, []).append(s)

        return list(hmap.values())