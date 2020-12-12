import torch
import numpy as np
import math

device = torch.device('cuda:0')

x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=torch.float)
y = torch.sin(x)

a = torch.randn((), device=device, dtype=torch.float, requires_grad=True)
b = torch.randn((), device=device, dtype=torch.float, requires_grad=True)
c = torch.randn((), device=device, dtype=torch.float, requires_grad=True)
d = torch.randn((), device=device, dtype=torch.float, requires_grad=True)

lr = 1e-6
for i in range(2000):
    y_pred = a + b * x + c * x**2 + d * x**3

    loss = (y_pred - y).pow(2).sum()

    if i%100 == 99:
        print(f'{i}: {loss.item()}')
    
    loss.backward()

    with torch.no_grad():
        a -= lr * a.grad
        b -= lr * b.grad
        c -= lr * c.grad
        d -= lr * d.grad
        
        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None

print(f'Result y = {a} + {b}x + {c}x^2 + {d}x^3')
