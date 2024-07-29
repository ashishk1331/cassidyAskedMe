# Question 363

# Write a function that converts between metric and 
# imperial units. Break up the units into millimeters, 
# centimeters, and meters for metric, and into inches 
# and feet for imperial, up to 2 decimal places.

table = {
	"ft": 0.3048, # m
	"in": 0.0254, # m

	"m": 3.28084, # ft
	"cm": 0.0328084, # ft
	"mm": 0.00328084, # ft
}

def format_m(value):
	result = []

	in_m = int(value)
	if in_m > 0:
		result.append(str(in_m) + "m")

	in_cm = int(value * 100 % 100)
	if in_cm > 0:
		result.append(str(in_cm) + "cm")

	in_mm = round(((value - in_m) * 100 - in_cm) * 1000) / 100
	if in_mm > 0:
		result.append(str(in_mm) + "mm")

	return " ".join(result)

def format_ft(value):
	result = []

	in_ft = int(value)
	if in_ft > 0:
		result.append(str(in_ft) + "ft")

	in_in = round((value - in_ft) * 12, 2)
	if in_in > 0:
		result.append(str(in_in) + "in")

	return " ".join(result)

def convertUnits(value, unit):
	if unit in ["ft", "in"]:
		return format_m(value * table[unit])
	else:
		return format_ft(value * table[unit])

def main():
	assert convertUnits(7, "ft") == "2m 13cm 3.6mm"
	assert convertUnits(44, "cm") == "1ft 5.32in"

if __name__ == '__main__':
	main()