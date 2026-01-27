class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


#This is your local test block
if __name__ == "__main__":
    sol = Solution()
    # Replace with sample inputs from the problem description
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew"
    ]
    for string in test_cases:
        print(f"Result: {sol.lengthOfLongestSubstring(string)}")