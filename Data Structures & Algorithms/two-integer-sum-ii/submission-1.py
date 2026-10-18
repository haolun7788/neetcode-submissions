class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hset = {}
        for n in range(len(numbers)):
            diff = target - numbers[n]
            if numbers[n] in hset:
                return [hset[numbers[n]] + 1, n + 1]
            else:
                hset[diff] = n
        return 0
                