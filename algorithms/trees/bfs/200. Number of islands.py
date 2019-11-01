# Reference: https://leetcode.com/problems/number-of-islands/
# Approach:
# 1. Get a list of all locations that have 1 
# 2. Iterate through this list and call DFS for every unmarked / unvisited 1 and mark all it's reachable locations with the current_island_count
# 3. The final value of current_island_count is the answer

class Solution(object):
    grid = []
    visited_dict = {}
    rowLen = 0
    colLen = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        islandCount = 0
        land_locations = []
        self.rowLen = len(grid)
        self.colLen = len(grid[0])       # considering symmetric matrix. Also add defensive condition on index 0 access

        for row in range(self.rowLen):
            for col in range(self.colLen):
                if grid[row][col] == "1":
                    land_locations.append((row, col))
        
        for (row, col) in land_locations:
            # if already visited, do not recurse on marking
            if (row, col) not in self.visited_dict:
                islandCount += 1
                print((row, col))
                print(islandCount)
                # mark self and neighbours
                self.markNeighbours(row, col, islandCount)
        return islandCount

    def markNeighbours(self, row, col, islandCountMarker):
        # first mark self
        self.visited_dict[(row, col)] = islandCountMarker
        # check whether neighbours exist and mark if it's a piece of connected land 
        if row + 1 < self.rowLen and self.grid[row + 1][col] == "1":
            self.markNeighbours(row + 1, col, islandCountMarker)
        if col + 1 < self.colLen and self.grid[row][col + 1] == "1":
            self.markNeighbours(row, col + 1, islandCountMarker)     
    
obj = Solution()
obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])   # Output: 1
obj.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])   # Output: 3 (switching between 2 & 3. Error only happened when string "1" used. May be due to the way DFS is being called. Check)    
