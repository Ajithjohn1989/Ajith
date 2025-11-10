import copy

a = [[1, 2, 3], [4, 5]]
b = copy.deepcopy(a)
b[1][0] = 99

print("Original:", a) # [[1, 2, 3], [4, 5, 6]]
print("Deep Copy:", b) # [[99, 2, 3], [4, 5, 6]]