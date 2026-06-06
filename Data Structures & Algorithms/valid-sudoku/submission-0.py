class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #9x9 board
    
        for r in range(9):
            if not self.is_valid(board[r]):
                return False
        
        for c in range(9):                                  
            column = [board[r][c] for r in range(9)]
            if not self.is_valid(column):
                return False
        
        for bi in range(3):                                 # 3x3 boxes
            for bj in range(3):
                box = [board[3*bi + dr][3*bj + dc]
                       for dr in range(3) for dc in range(3)]
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