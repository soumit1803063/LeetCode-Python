import sys
from solution import Solution

sol = Solution()
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

row, col = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(row)]
ret = sol.solve(grid)
print(grid)
sys.stdin.close()
sys.stdout.close()
