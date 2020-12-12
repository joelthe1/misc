import torch
import numpy as np
import math

device = torch.device('cuda:0')

x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=torch.float)
y = torch.sin(x)

a = torch.randn((), device=device, dtype=torch.float)
b = torch.randn((), device=device, dtype=torch.float)
c = torch.randn((), device=device, dtype=torch.float)
d = torch.randn((), device=device, dtype=torch.float)

lr = 1e-6
for i in range(2000):
    y_pred = a + b * x + c * x**2 + d * x**3

    loss = (y_pred - y).pow(2).sum().item()

    if i%100 == 99:
        print(f'{i}: {loss}')

    y_pred_grad = 2.0 * (y_pred-y)
    da = y_pred_grad.sum()
    db = (y_pred_grad * x).sum()
    dc = (y_pred_grad * x**2).sum()
    dd = (y_pred_grad * x**3).sum()

    a -= lr * da
    b -= lr * db
    c -= lr * dc
    d -= lr * dd

print(f'Result y = {a} + {b}x + {c}x^2 + {d}x^3')
