def removeDigit(n, k):
	num = str(n)
	target = str(k)
	amx = 0
	for i in range(len(num)):
		if num[i] == target:
			amx = max(amx, int(num[:i] + num[i+1:]))
	return amx

def main():
	assert removeDigit(31415926, 1) == 3415926
	assert removeDigit(1231, 1) == 231

if __name__ == '__main__':
	main()