class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = collections.Counter(s)

        for char in t:
            s[char] -= 1

        for count in s.values():
            if count != 0:
                return False

        return True


# Time complexity: O(len(s))
# Space complexity: O(len(s))
