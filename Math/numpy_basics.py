import numpy as np

# ----------------------------
# VECTORS
# ----------------------------

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

# ----------------------------
# 1. Addition
# ----------------------------

addition = v1 + v2
print("\nAddition:")
print(addition)

# ----------------------------
# 2. Subtraction
# ----------------------------

subtraction = v1 - v2
print("\nSubtraction:")
print(subtraction)

# ----------------------------
# 3. Dot Product
# ----------------------------

dot_product = np.dot(v1, v2)
print("\nDot Product:")
print(dot_product)

# ----------------------------
# 4. Norm (Magnitude)
# ----------------------------

norm_v1 = np.linalg.norm(v1)
print("\nNorm of Vector 1:")
print(norm_v1)

# ----------------------------
# 5. Distance Between Two Vectors
# ----------------------------

distance = np.linalg.norm(v1 - v2)
print("\nEuclidean Distance:")
print(distance)

# ----------------------------
# MATRICES
# ----------------------------

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# ----------------------------
# 6. Matrix Multiplication
# ----------------------------

matrix_product = np.matmul(A, B)
# or A @ B

print("\nMatrix Multiplication:")
print(matrix_product)

# ----------------------------
# 7. Transpose
# ----------------------------

transpose = A.T

print("\nTranspose:")
print(transpose)

# ----------------------------
# 8. Inverse
# ----------------------------

inverse = np.linalg.inv(A)

print("\nInverse:")
print(inverse)

# ----------------------------
# 9. Determinant
# ----------------------------

determinant = np.linalg.det(A)

print("\nDeterminant:")
print(determinant)