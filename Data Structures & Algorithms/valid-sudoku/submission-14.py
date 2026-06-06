class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A board is valid if:
        # 1. every row has no duplicate digits
        # 2. every column has no duplicate digits
        # 3. every 3x3 box has no duplicate digits

        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # Check each 3x3 box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen.add(val)

        return True
