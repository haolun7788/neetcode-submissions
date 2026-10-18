class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def doRecur(nums: List[int], path: List[int], start: int):
            if sum(path) == target:
                newPath = path.copy()
                out.append(newPath)
                return
            
            if sum(path) > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                doRecur(nums, path, i)
                path.pop()
                

        doRecur(nums, [], 0)
            
        return out
