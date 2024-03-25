def largestIsland(map):
	rows, cols = len(map), len(map[0])
	visited = set()

	def dfs(r, c):
		if (
			r in range(rows) and
			c in range(cols) and
			(r, c) not in visited and
			map[r][c]
		):
			visited.add((r, c))
			return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
		return 0

	max_area = 0
	for i in range(rows):
		for j in range(cols):
			if map[i][j] == 1 and (i, j) not in visited:
				max_area = max(max_area, dfs(i, j))

	return max_area

def main():
	map = [
		[0,1,1,1,0,0,0,1,1],
		[0,1,1,1,0,1,0,0,0],
		[0,1,0,0,0,0,0,1,0],
		[0,0,1,1,0,1,1,1,0],
	]

	assert largestIsland(map) == 7

if __name__ == '__main__':
	main()