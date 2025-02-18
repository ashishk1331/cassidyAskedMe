# Question for Week 391
from typing import List

LEGEND = {
	"QB": [(0, 19)],
	"RB": [(0, 49), (80, 89)],
	"WR": [(0, 49), (80, 89)],
	"TE": [(0, 49), (80, 89)],
	"OL": [(50, 79)],
	"DL": [(50, 79), (90, 99)],
	"LB": [(0, 59), (90, 99)],
	"DB": [(0, 49)],
	"K/P": [(0, 49), (90, 99)],
	"LS": [(0, 99)],
}

def availableNumbers(pos: str, taken: List[int]) -> List[int]:
	total = set(range(1, 100)) - set(taken)
	permitable = set()
	for r in LEGEND[pos]:
		permitable = permitable | set(range(*r))
	return list(sorted(total & permitable))

def main():
	assert availableNumbers("QB", [1, 2, 3, 10, 19]) == [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]

if __name__ == '__main__':
	main()