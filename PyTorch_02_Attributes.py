import torch

# Initializing a 3x4 tensor
tensor_1 = torch.rand(3,4)
print('Tensor 1:\n', tensor_1)

# Attributes
print('Shape of tensor:', tensor_1.shape)
print('Datatype of tensor:', tensor_1.dtype)
print('Device tensor is stored on:', tensor_1.device)

# Initializing a tensor with ones
tensor_2 = torch.ones(3, 4)
print('Tensor 2:\n', tensor_2)

print('First row:', tensor_2[0])
print('First column:', tensor_2[:, 0])
print('Last column:', tensor_2[..., -1])

# Joining tensors
tensor_3 = torch.cat([tensor_1, tensor_2], dim=1)
print('Tensor 1 and 2 joined:\n', tensor_3)
