hpos = 0
depth = 0
with open('input.txt', 'r') as f:
    for line in f:
        direction, distance = line.strip().split(' ')
        distance = int(distance)
        if direction == 'forward':
            hpos += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance
print('Task 1:', hpos * depth)



hpos = 0
depth = 0
aim = 0
with open('input.txt', 'r') as f:
    for line in f:
        direction, distance = line.strip().split(' ')
        distance = int(distance)
        if direction == 'forward':
            hpos += distance
            depth +=  aim * distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
print('Task 2:', hpos * depth)

