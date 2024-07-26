# Question 351

# Write a "word wrapping" function that takes in 
# a string and the maximum width of a line of text, 
# and return the text "wrapped" to that line length. 
# Include dashes for broken words (which is included 
# 	in the length of that line), and don't let a 
# line start with a non-alphanumeric character.

def wrap(string, width):
	result = ""
	temp = ""
	n = len(string)

	for index, char in enumerate(string):
		if len(temp) == width:
			leftover = ""
			if index < n and temp[-1].isalnum() and char.isalnum():
				leftover = temp[-1]
				temp = temp[:-1] + "-"

			result += temp + "\n"
			temp = "" + leftover

		temp += char

	return result + temp

def main():
	assert wrap("Hello, world! I am hungry.", 10) == "Hello, wo-\nrld! I am \nhungry."

if __name__ == '__main__':
	main()