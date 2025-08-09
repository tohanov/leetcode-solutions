class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()

        for i, num1 in enumerate(nums):
            needed_num2 = target - num1

            if (j := num_to_index.get(needed_num2)) is not None:
                return j, i

            num_to_index[num1] = i

        # unreachable since always exactly one solution exists
