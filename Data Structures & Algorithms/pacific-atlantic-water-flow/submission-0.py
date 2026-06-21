class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get row count
        rows = len(heights)

        # get column count
        cols = len(heights[0])

        # cells reachable from Pacific
        pacific = set()

        # cells reachable from Atlantic
        atlantic = set()

        # define dfs
        def dfs(row, col, visited):
            # mark current cell
            visited.add((row, col))

            # possible moves
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            # try each direction
            for dr, dc in directions:
                # compute next row
                new_row = row + dr

                # compute next column
                new_col = col + dc

                # skip out of bounds
                if new_row < 0 or new_row == rows or new_col < 0 or new_col == cols:
                    continue

                # skip already visited
                if (new_row, new_col) in visited:
                    continue

                # skip lower cells
                if heights[new_row][new_col] < heights[row][col]:
                    continue

                # continue uphill
                dfs(new_row, new_col, visited)

        # start from left and right borders
        for row in range(rows):
            # pacific left edge
            dfs(row, 0, pacific)

            # atlantic right edge
            dfs(row, cols - 1, atlantic)

        # start from top and bottom borders
        for col in range(cols):
            # pacific top edge
            dfs(0, col, pacific)

            # atlantic bottom edge
            dfs(rows - 1, col, atlantic)

        # store answer
        result = []

        # check every cell
        for row in range(rows):
            # scan columns
            for col in range(cols):
                # reachable from both oceans
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        # return result
        return result