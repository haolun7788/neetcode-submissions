class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int(left + (right - left) / 2)

            # the middle value is on right side of the rotation, target value is on right side of the rotation
            mfac, tfac = nums[mid] <= nums[len(nums) - 1], target <= nums[len(nums) - 1]
            
            if (mfac and tfac) or (not mfac and not tfac):
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif not mfac and tfac:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


