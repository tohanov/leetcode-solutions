class Solution:
    def bitset_mark(self, bitset, digit):
        return bitset | (1 << (digit - 1))

    def row_iterator(self, i):
        for digit in self.board[i]:
            if digit == ".":
                continue
            yield int(digit)

    def column_iterator(self, j):
        for row in self.board:
            digit = row[j]
            if digit == ".":
                continue
            yield int(digit)

    def square_iterator(self, square_i, square_j):
        # the bounds of a single 3x3 square are:
        # from board[3*i, 3*j]
        # to board[3*i + 3, 3*j + 3], not inclusive

        j_low_bound, j_high_bound = 3 * square_j, 3 * square_j + 3

        for i in range(3 * square_i, 3 * square_i + 3):
            for j in range(j_low_bound, j_high_bound):
                digit = self.board[i][j]
                if digit == ".":
                    continue
                yield int(digit)

    def is_unique_collection(self, iterator):
        bitset = 0

        for digit in iterator:
            new_bitset = self.bitset_mark(bitset, digit)

            if new_bitset == bitset:
                return False

            bitset = new_bitset

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board

        for i in range(9):
            if not (
                self.is_unique_collection(self.row_iterator(i))
                and self.is_unique_collection(self.column_iterator(i))
            ):
                return False

        for i in range(3):
            for j in range(3):
                if not self.is_unique_collection(self.square_iterator(i, j)):
                    return False

        return True
