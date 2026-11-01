class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())

def normalize(result):
    return sorted(sorted(group) for group in result)

if __name__ == "__main__":
    sol = Solution()

    result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(result)