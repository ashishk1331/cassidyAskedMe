def evaluatePostfix(expression: str) -> int:
	stack = []
	operations = {
		"+": lambda x, y: x + y,
		"-": lambda x, y: x - y,
		"*": lambda x, y: x * y,
		"/": lambda x, y: x // y,
	}
	for char in expression:
		if char.isalnum():
			stack.append(int(char))
		else:
			b, a = stack.pop(), stack.pop()
			stack.append(operations[char](a, b))
	return stack[-1]
			

def main():
	assert evaluatePostfix('12+') == 3
	assert evaluatePostfix('56+7*') == 77
	print("✅ All tests passed.")

if __name__ == '__main__':
	main()