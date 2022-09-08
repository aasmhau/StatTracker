
class Solution:

    def searchInsert(self, nums, target) -> int:
        while (len(nums) > 2):
            if (target > nums[len(nums)/2]):
                nums = nums[len(nums):]
            else:
                nums = nums[:len(nums)]
            print(nums)


def main():
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 7], 2))
    assert sol.searchInsert([1, 3, 5, 7], 2) == 1
