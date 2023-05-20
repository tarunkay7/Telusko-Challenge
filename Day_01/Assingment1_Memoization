def pascals_triangle_memo(num_rows, memo={}):
    if num_rows == 1:
        return [[1]]

    if num_rows in memo:
        return memo[num_rows]

    tri = pascals_triangle_memo(num_rows - 1, memo)
    prev_row = tri[-1]
    row = [1]

    for i in range(len(prev_row) - 1):
        row.append(prev_row[i] + prev_row[i + 1])

    row.append(1)
    tri.append(row)

    memo[num_rows] = tri

    return tri

def main():
    num_rows = 6
    result = pascals_triangle_memo(num_rows)
    for row in result:
        print(row)
