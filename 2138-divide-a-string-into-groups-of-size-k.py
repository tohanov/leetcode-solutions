class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = list()

        groups_count = len(s) // k
        iteration_bound = groups_count * k

        for slice_begin in range(0, iteration_bound, k):
            groups.append(s[slice_begin : slice_begin + k])

        if len(s) > iteration_bound:
            missing_chars_count = k - (len(s) - iteration_bound)
            groups.append(s[iteration_bound:] + fill * missing_chars_count)

        return groups
