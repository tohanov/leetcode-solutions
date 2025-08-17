class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = 0
        ep = len(s) - 1

        while sp < ep:
            if not s[sp].isalnum():
                while sp < ep and not s[sp].isalnum():
                    sp += 1
            if not s[ep].isalnum():
                while ep > sp and not s[ep].isalnum():
                    ep -= 1

            if not sp < ep:
                break

            if s[sp].lower() != s[ep].lower():
                return False

            sp += 1
            ep -= 1

        return True


# Time complexity: O(len(s))
# Space complexity: O(1)
