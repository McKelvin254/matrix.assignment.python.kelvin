import numpy as np

A = np.array([ [2,5],
               [4,7] ])

B = np.array([ [3,8],
               [9,2] ])

print("Matrix : A")
print(A)

print("Matrix : B")
print(B)

elementwise_add = A + B

print("Elementwise addition(A + B)")
print(elementwise_add)

elementwise_multiplication = A * B
print("Element multiplication(A * B)")
print(elementwise_multiplication)

matrix_product = A @ B
print("Matrix multiplication(A @ B)")
print(matrix_product)