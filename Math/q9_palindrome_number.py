class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        div = 1

        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div = div / 100
        return True


#This is your local test block
if __name__ == "__main__":
    sol = Solution()
    # Replace with sample inputs from the problem description
    test_cases = [
        1000021,
        121,
        0
    ]
    for num in test_cases:
        print(f"Result: {sol.isPalindrome(num)}")