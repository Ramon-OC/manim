edges = [
(0,1),
(0,2),
(1,3),
(1,4),
(2,3),
(3,4)
]

import cvxpy as cp
import numpy as np
from scipy.linalg import sqrtm


X = cp. Variable((5, 5), symmetric=True)
constraints = [X >> 0]
constraints += [
X[i, i] == 1 for i in range(5)
]
objective = sum( 0.5*(1 - X[i, j]) for (i, j) in edges )
prob = cp.Problem(cp.Maximize(objective), constraints)
prob.solve()

print(X.value)

x = sqrtm(X.value)
print(x)

u = np. random.randn(5) # normal to a random hyperplane
x = np.sign(x @ u)
