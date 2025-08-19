class Solution:
    def reverseBits(self, n: int) -> int:
        # binary_n = bin(n)[2:]
        # binary_n = '0' * (32 - len(binary_n)) + binary_n
        # return int(''.join(reversed(binary_n)), 2)
        ############################

        # return int("".join(reversed("{:032b}".format(n))), 2)

        ############################
        reversed_int = 0

        for _ in range(32):
            lsb = n % 2
            n >>= 1
            reversed_int <<= 1
            reversed_int |= lsb

        return reversed_int


# Time complexity: O(32) = O(1)
# Space complexity: O(1)
