class HexGrid:
    def __init__(self, L, N, M):
        self.L = L
        self.N = N
        self.M = M
        self.grid = [[0] * N for _ in range(M)]
    
    def print_grid(self):
        for row in self.grid:
            print(row)
import random

def fill_grid(grid, p):
    for i in range(grid.M):
        for j in range(grid.N):
            if random.random() < p:
                grid.grid[i][j] = 1
def count_domains(grid):
    visited = [[False] * grid.N for _ in range(grid.M)]
    count = 0

    def is_valid(i, j):
        return i >= 0 and i < grid.M and j >= 0 and j < grid.N and grid.grid[i][j] == 1 and not visited[i][j]

    def dfs(i, j):
        nonlocal visited
        visited[i][j] = True

        # смежные ячейки
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j+1), (i+1, j-1)]
        
        for ni, nj in neighbors:
            if is_valid(ni, nj):
                dfs(ni, nj)

    for i in range(grid.M):
        for j in range(grid.N):
            if grid.grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count
def count_disconnected_domains(grid):
    visited = [[False] * grid.N for _ in range(grid.M)]
    count = 0

    def is_valid(i, j):
        return i >= 0 and i < grid.M and j >= 0 and j < grid.N and grid.grid[i][j] == 1 and not visited[i][j]
    
    def has_hole(i, j):
        nonlocal visited
        visited[i][j] = True

        # смежные ячейки
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j+1), (i+1, j-1)]
        
        for ni, nj in neighbors:
            if is_valid(ni, nj):
                return True
        
        return False

    for i in range(grid.M):
        for j in range(grid.N):
            if grid.grid[i][j] == 1 and not visited[i][j]:
                if has_hole(i, j):
                    count += 1

    return count
grid = HexGrid(3, 5, 7)
fill_grid(grid, 0.5)
grid.print_grid()

num_domains = count_domains(grid)
print("Количество доменов:", num_domains)

num_disconnected_domains = count_disconnected_domains(grid)
print("Количество неодносвязных доменов:", num_disconnected_domains)
