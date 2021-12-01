import numpy as np

def cnt_increase(numbers):
    inc = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            inc += 1
    return inc

with open('input', 'r') as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines]

print('Task 1:', cnt_increase(numbers))


numbers = np.array(numbers)
numbers = np.convolve(numbers, np.array([1, 1, 1]), mode='valid')


print('Task 2:', cnt_increase(numbers))
