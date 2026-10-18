class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = []
        rtl = []

        for n in range(len(nums)):
            if n == 0:
                ltr.append(1)
            else:
                ltr.append(nums[n - 1] * ltr[n - 1])
        
        for n in range(len(nums) - 1, -1, -1):
            if n == len(nums) - 1:
                rtl.append(1)
            else:
                rtl.append(nums[n + 1] * rtl[len(nums) - 1 - n - 1])
            
        rtl.reverse()
        for n in range(len(rtl)):
            ltr[n] = ltr[n] * rtl[n]
        
        return ltr