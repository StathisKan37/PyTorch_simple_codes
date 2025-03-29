import torch
import numpy as np

# Initializing a tensor, directly from data
tensor_1 = torch.tensor([[1, 2],[3, 4]])
print('Tensor:\n', tensor_1)

# Initializing a tensor, from a NumPy array
np_array = np.array([[1, 2],[3, 4]])
tensor_2 = torch.from_numpy(np_array)
print('Numpy tensor:\n', tensor_2)

# Initializing a tensor with ones, from another tensor
tensor_3 = torch.ones_like(tensor_2)
print('Tensor with ones:\n', tensor_3)

# Initializing a tensor with random floats, from another tensor
tensor_4 = torch.rand_like(tensor_2, dtype=torch.float)
print('Tensor with random floats:\n', tensor_4)

# Tensors with specific shape
tensor_shape = (2,3)

tensor_5 = torch.rand(tensor_shape)
print('2x3 Tensor with random floats:\n', tensor_5)

tensor_6 = torch.ones(tensor_shape)
print('2x3 Tensor with ones:\n', tensor_6)

tensor_7 = torch.zeros(tensor_shape)
print('2x3 Tensor with zeros:\n', tensor_7)
