def pascals_triangle(num_rows):
    tri = []
    for i in range(num_rows):
        row = [1]
        if tri:
            prev_row = tri[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        tri.append(row)
    return tri


def main():
    num_rows = 6
    result = pascals_triangle(num_rows)
    for row in result:
        print(row)


main()
