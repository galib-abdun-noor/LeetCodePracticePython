from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], n]
            prevMap[n] = i

        return

#This is your local test block
if __name__ == "__main__":
    sol = Solution()
    # Replace with sample inputs from the problem description
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6)
    ]
    for nums, target in test_cases:
        print(f"Result: {sol.twoSum(nums, target)}")