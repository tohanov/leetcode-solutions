class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        ans = [0, 1]
        looping_pointer = 0
        ans_len = len(ans)

        for i in range(2, n + 1):
            ans.append(ans[looping_pointer] + 1)

            if looping_pointer == ans_len - 1:
                looping_pointer = 0
                ans_len = len(ans)
            else:
                looping_pointer += 1

        return ans


# Time complexity: O(n)
# Space complexity: O(n) if including the returned structure, else O(1)
