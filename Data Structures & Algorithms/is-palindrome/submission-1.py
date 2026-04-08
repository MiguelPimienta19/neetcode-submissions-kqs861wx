class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase to make the comparison case-insensitive
        s = s.lower()

        # Base case: if the string has 1 or 0 characters, it's a palindrome
        if len(s) <= 1:
            return True

        # Check if the first character is not alphanumeric, skip it
        if not s[0].isalnum():
            return self.isPalindrome(s[1:])

        # Check if the last character is not alphanumeric, skip it
        if not s[-1].isalnum():
            return self.isPalindrome(s[:-1])

        # Compare the first and last characters
        if s[0] != s[-1]:
            return False

        # Recursively check the substring excluding the first and last characters
        return self.isPalindrome(s[1:-1])
