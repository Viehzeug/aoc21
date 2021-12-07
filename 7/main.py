import numpy as np

pos = np.fromfile('input.txt', sep=',', dtype=np.int)

least_i, least_cost = 0, np.inf
for i in range(pos.max()+1):
    cost = np.abs(pos-i).sum()
    if cost < least_cost:
        least_i, least_cost = i, cost

print('Task 1:', least_i, least_cost)

def f(delta):
    delta = delta.astype(np.float64)
    return (delta) * ((delta+1)/2)
 

least_i, least_cost = 0, np.inf
for i in range(pos.max()+1):
    cost = f(np.abs(pos-i)).sum()
    if cost < least_cost:
        least_i, least_cost = i, int(cost)


print('Task 2:', least_i, least_cost)

