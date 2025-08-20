class Solution:
    def hammingWeight(self, n: int) -> int:
        sum_1s = 0

        while n > 0:
            sum_1s += n % 2
            n >>= 1

        return sum_1s


# Time complexity: O(31) = O(1)
# Space complexity: O(1)
