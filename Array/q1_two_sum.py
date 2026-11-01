from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return

#Local test block
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6)
    ]
    for nums, target in test_cases:
        print(f"Result: {sol.twoSum(nums, target)}")