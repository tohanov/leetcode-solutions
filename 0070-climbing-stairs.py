class Solution:
    def climbStairs(self, n: int) -> int:
        for_staircase_minus_1 = 2
        for_staircase_minus_2 = 1

        if n == 0:
            return 0
        if n == 1:
            return for_staircase_minus_2
        if n == 2:
            return for_staircase_minus_1

        for _ in range(3, n + 1):
            for_staircase_i = for_staircase_minus_1 + for_staircase_minus_2

            for_staircase_minus_1, for_staircase_minus_2 = (
                for_staircase_i,
                for_staircase_minus_1,
            )

        return for_staircase_minus_1


# T: O(n)
# S: O(1)
