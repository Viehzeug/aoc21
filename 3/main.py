import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
    cnt = len(lines)
    n = len(lines[0].strip())
    data = np.zeros((cnt, n))
    for i, line in enumerate(lines):
        for j, p in enumerate(line.strip()):
            if p == '1':
                data[i, j] = 1
bits = data.sum(axis=0) > cnt/2
powers = np.power(2, np.arange(n-1, -1, -1))
gamma = (bits * powers).sum()
epsilon = ((1-bits) * powers).sum()
print('Task 1:', epsilon * gamma)

def get_value(negate=False):
    curr_data = data
    for i in range(n):
        criteria = int(curr_data[:, i].sum() >= curr_data.shape[0]/2)
        if negate: criteria = 1 - criteria
        curr_data = curr_data[curr_data[:, i] == criteria, ...]
        if curr_data.shape[0] == 1: break
    return int((curr_data * powers).sum())

oxygen = get_value()
co2 = get_value(negate=True)
print('Task 2:', oxygen * co2)
