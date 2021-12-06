import numpy as np 
def step(fish):
    fish = fish-1
    I = (fish < 0)
    new_cnt = I.sum()
    fish[I] = 6 # don't want to mod as else we reset 7 to 0
    #fish = np.mod(fish-1, 7)
    fish = np.append(fish, [8]*new_cnt, 0).astype(np.int32)
    return fish

def steps_fast(fish, n):

    memoization = np.full((8+1, n+1), -1, dtype=np.int64)
    def f(i, n):
        if memoization[i, n] == -1:
            if n == 0:   v = 1
            elif i == 0: v = f(8, n-1) + f(6, n-1)
            else:        v = f(i-1, n-1)
            memoization[i, n] = v
        return memoization[i, n]

    cnt = 0
    for fi in fish:
        cnt += f(fi, n)
    return cnt


with open('input.txt', 'r') as f:
    initialfish = np.fromstring(f.read(), dtype=np.int32, sep=',')

fish = initialfish.copy()
for i in range(80):
    fish = step(fish)
    #print(i+1, fish.tolist())
print('Task 1:', fish.size)
print('Task 1 (fast):', steps_fast(initialfish, 80))


print('Task 2:', steps_fast(initialfish, 256))






