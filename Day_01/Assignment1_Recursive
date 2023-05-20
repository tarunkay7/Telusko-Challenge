def pascals_triangle_recursive(num_rows):
    if num_rows == 1:
        return [[1]]
    tri = pascals_triangle_recursive(num_rows - 1)
    prev_row = tri[-1]
    row = [1]

    for i in range(len(prev_row) - 1):
        row.append(prev_row[i] + prev_row[i + 1])
    row.append(1)
    tri.append(row)
    return tri


def main():
    num_rows = 6
    result = pascals_triangle_recursive(num_rows)
    for row in result:
        print(row)
