class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have same length
        if len(s) != len(t):
            return False

        # Count each character in s, subtract counts for t
        counts = [0] * 26
        for i, j in zip(s, t):
            counts[ord(i) - ord("a")] += 1
            counts[ord(j) - ord("a")] -= 1

        # Every count must order out to zero
        return all(c == 0 for c in counts)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "cat"))