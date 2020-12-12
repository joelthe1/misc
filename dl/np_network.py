#
# Create a simple neural network with only Numpy
#
import numpy as np
import math

x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

a = np.random.rand()
b = np.random.rand()
c = np.random.rand()
d = np.random.rand()

lr = 1e-6

for i in range(2000):
    y_pred = a + b * x + c * x**2 + d * x**3

    loss = np.square(y_pred - y).sum()

    if i%100 == 99:
        print(f'{i}: {loss}')

    y_pred_grad = 2.0 * (y_pred - y)
    da = y_pred_grad.sum()
    db = (y_pred_grad * x).sum()
    dc = (y_pred_grad * x ** 2).sum()
    dd = (y_pred_grad * x ** 3).sum()

    a -= lr * da
    b -= lr * db
    c -= lr * dc
    d -= lr * dd

print(f'Results y = {a} + {b}x + {c}x^2 + {d}x^3')
