import torch

# Initializing a tensor
tensor_1 = torch.tensor([[1,2,3],[4,5,6]])
print('Tensor 1:\n', tensor_1)

# The first tensor transposed
tensor_2 = tensor_1.T
print('Tensor 2:\n', tensor_2)

# Initializing another tensor
tensor_3 = torch.tensor([[2,4,6],[8,10,12]])
print('Tensor 3:\n', tensor_3)

# Matrix multiplication with 3 different ways
# tensor_1 * tensor_2 = [[14, 32],
#                        [32, 77]]
print('Tensor multiplication:')

tensor_mat_mul_1 = tensor_1 @ tensor_2
print(tensor_mat_mul_1)

tensor_mat_mul_2 = tensor_1.matmul(tensor_2)
print(tensor_mat_mul_2)

tensor_mat_mul_3 = torch.matmul(tensor_1, tensor_2)
print(tensor_mat_mul_3)

# Element multiplication
# tensor_1 * tensor_3 = [[ 2,  8, 18],
#                        [32, 50, 72]]
print('Element multiplication')

tensor_mul_1 = tensor_1 * tensor_3
print(tensor_mul_1)

tensor_mul_2 = tensor_1.mul(tensor_3)
print(tensor_mul_2)

tensor_mul_3 = torch.mul(tensor_1, tensor_3)
print(tensor_mul_3)

# Sum of tensor_1 elements
print('Sum of tensor 1 elements:', tensor_1.sum())

# Adding 5 at tensor 1
tensor_4 = tensor_1.add_(5)
print('Tensor 4:\n', tensor_4)
