from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))