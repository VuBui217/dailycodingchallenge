def pacificAtlantic(heights):
       # Sets which represent true for pacific and atlantic
       # TBD
       reach_pacific = set()
       reach_atlantic = set()
       visited = set()


       for i in range(len(heights)):
           for j in range(len(heights[0])):
               cell = (i, j)
               # Do the DFS
               dfs(cell, heights, visited, reach_pacific, reach_atlantic)
      
       # Get the set intersection and return
       result = reach_pacific.intersection(reach_atlantic)


       # Convert to list
       return [[x, y] for (x, y) in result]
  
def dfs(cell, heights, visited, reach_pacific, reach_atlantic):
    # Stop condition for the DFS
    # Cell in visited
    if cell in visited:
        return
    visited.add(cell)
    # Cell is next to either ocean
    can_reach_pacific = False
    can_reach_atlantic = False
    if cell in reach_pacific or adjacent_pacific(cell, heights):
        can_reach_pacific = True
        reach_pacific.add(cell)
    if cell in reach_atlantic or adjacent_atlantic(cell, heights):
        can_reach_atlantic = True
        reach_atlantic.add(cell)
    if can_reach_pacific and can_reach_atlantic:
        return
   
    # Start the DFS for each cell less than or equal to current cell
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_cell = tuple(x + y for x, y in zip(cell, dir))
        # Don't add if cell outside boundary
        if within_bounds(new_cell, heights) and lower_heights(cell, new_cell, heights):
            dfs(new_cell, heights, visited, reach_pacific, reach_atlantic)
            # Neighbor can reach pacific
            if new_cell in reach_pacific:
                # So, current cell can also reach pacific
                reach_pacific.add(cell)
            if new_cell in reach_atlantic:
                # So, current cell can also reach pacific
                reach_atlantic.add(cell)
def adjacent_pacific(cell, heights):
    return cell[0] == 0 or cell[1] == 0

def adjacent_atlantic(cell, heights):
    return cell[0] == len(heights) - 1 or cell[1] == len(heights[0]) - 1

def within_bounds(cell, heights):
    return cell[0] >= 0 and cell[0] < len(heights) and cell[1] >= 0 and cell[1] < len(heights[0])

def lower_heights(current_cell, new_cell, heights):
    return heights[new_cell[0]][new_cell[1]] <= heights[current_cell[0]][current_cell[1]]



heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[1,1,1,2,4]]
# output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(pacificAtlantic(heights))