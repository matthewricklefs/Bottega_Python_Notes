### First Solution
# def manual_incrementing_matrix(n):
#     matrix = [ [ None for y in range(n) ] for x in range(n) ]

#     counter = 0

#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix[idx][nested_idx] = counter + nested_idx

#         counter += 1

#     return matrix

# print(manual_incrementing_matrix(5))

### 2nd approach
import numpy as np

morpheus = np.array(range(1,10,1)).reshape(3,3)

print(morpheus)


columns = []
grid = []

num_of_rows = 3
num_of_columns = 4

### 3rd approach

#creates the matrix
for x in range(0, num_of_rows): # 3 rows by 4 columns
    for y in range(0, num_of_columns): 
        columns.append((x, y))
    grid.append(columns.copy())
    columns = []

#prints the grid in the matrix format
for x in range(0, len(grid)):
    print(grid[x])