def count_vowels(name):
	count = 0
	for char in name:
		if char.lower() in "aeiou":
			count += 1
	return count

def sortNames(names):
	result = sorted(names, key=count_vowels)
	result.reverse()
	return result

def main():
	assert sortNames(["Goku", "Vegeta", "Piccolo", "Gohan"]) == ["Piccolo", "Vegeta", "Gohan", "Goku"]
	assert sortNames(["Edward", "Alphonse", "Roy", "Winry"]) == ["Alphonse", "Edward", "Winry", "Roy"]

if __name__ == '__main__':
	main()