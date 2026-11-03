import ch


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()

    print(sol.isValid("()[]{}"))
    print(sol.isValid("([)]"))



