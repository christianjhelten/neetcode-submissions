class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #9x9 board
    
        for r in range(9):
            row = board[r]
            if not self.is_valid(row):
                return False

        # Check each column
        for c in range(9):
            column = []
            for r in range(9):
                column.append(board[r][c])
            if not self.is_valid(column):
                return False

        # Check each 3x3 box
        for box_row in range(0, 9, 3):           # 0, 3, 6
            for box_col in range(0, 9, 3):       # 0, 3, 6
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                if not self.is_valid(box):
                    return False
        
        return True

    def is_valid(self, frame):
        seen = set()
        for item in frame:
            if item == ".":
                continue
            if item in seen:
                return False        # duplicate found
            seen.add(item)
        return True