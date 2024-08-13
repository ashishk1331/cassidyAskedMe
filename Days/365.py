# Question 365

# Given an array of logs and variable assignments, 
# return a list of all unused variables.

from collections import defaultdict

def findUnused(cmds):
	dmap = defaultdict(list)
	dmap['log'] = []

	declared = set()

	for cmd in cmds:
		if cmd.startswith('log'):
			var = cmd[cmd.index('(') + 1: cmd.index(')')]
			dmap['log'].append(var)
		else:
			left, right = cmd.split(" = ")
			declared.add(left)
			if right.isalpha():
				dmap[left].append(right)

	used = set()
	def dfs(var):
		if var in used:
			return

		used.add(var)

		if var in dmap:
			for dependency in dmap[var]:
				dfs(dependency)

	for var in dmap['log']:
		if var not in used:
			dfs(var)

	unused = list(declared -  used)
	unused.sort()

	return unused

def main():
	assert findUnused(["a = 1", "b = a", "c = 2", "log(b)"]) == ["c"]
	assert findUnused(["a = 1", "b = a", "c = 2", "log(c)"]) == ["a", "b"]

if __name__ == '__main__':
	main()