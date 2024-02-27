MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def parse(date):
	rest, year = date.split(',')
	year = int(year.strip())
	rest = rest.split()
	month = MONTHS.index(rest[0])
	day = int(rest[1])
	return day, month, year

def daysBetween(date_one, date_two):
	date_one, date_two = parse(date_one), parse(date_two)
	diff = [0, 0, 0]
	diff[2] = date_two[2] - date_one[2]
	diff[2] = diff[2]*365 + diff[2]//4

	print(sum(diff))
	return sum(diff)

def main():
	assert daysBetween('Jan 1, 2024', 'Jan 29, 2024') == 28
	assert daysBetween('Feb 29, 2020', 'Oct 31, 2023') == 1340

if __name__ == '__main__':
	main()