def flip(matrix, direction):
    n, m = len(matrix), len(matrix[0])

    if direction == "horizontal":
        mid = m // 2
        for row in range(n):
            for col in range(mid + 1):
                matrix[row][col], matrix[row][m - 1 - col] = (
                    matrix[row][m - 1 - col],
                    matrix[row][col],
                )
    else:
        mid = n // 2
        for col in range(m):
            for row in range(mid + 1):
                matrix[row][col], matrix[n - 1 - row][col] = (
                    matrix[n - 1 - row][col],
                    matrix[row][col],
                )


def main():
    matrix = [[x for x in range(i + 1, i + 4)] for i in range(0, 9, 3)]
    print(matrix)

    flip(matrix, "horizontal")

    print("Horizontal: ", matrix)

    matrix = [[x for x in range(i + 1, i + 4)] for i in range(0, 9, 3)]
    flip(matrix, "vertical")

    print("Vertical: ", matrix)


if __name__ == "__main__":
    main()
