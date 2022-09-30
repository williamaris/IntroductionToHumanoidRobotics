import numpy as np

pi = np.array([1., 7.]).T
p = np.array([3., 6.]).T
fi = np.array([7., 8.])

print(np.matmul(pi - p, fi))
print(np.matmul(pi, fi) - np.matmul(p, fi))