def pascalTriangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = triangle[ i - 1][j - 1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

numRows = 5
result = pascalTriangle(numRows)
print(result)
for row in result:
    print(" ".join(map(str, row)).center(numRows * 4))