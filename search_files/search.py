#search

import state
import frontier

pushed = 0
popped = 0
depth = 0

def search(n):
    global pushed, popped, depth
    s=state.create(n)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            depth += f[1]
            pushed += f[4]
            popped += f[5]
            return [s, f[1]]
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
    return 0

# answer=search(4)

size = 3
for i in range(100):
    answer = search(size)
    # print(answer)
print("%sx%s grid: " % (size, size)) 
print("Average depth: " + str(depth/100.0)) 
print("Average states checked: " + str(pushed/100.0))
print("Average number popped: " + str(popped/100.0))

"""
=============================
OUTPUT
=============================
search(2)

2x2 grid: 
Average depth: 1.79
Average states checked: 5.5
Average number popped: 6.13

search(3)

3x3 grid: 
Average depth: 6.12
Average states checked: 830.66
Average number popped: 828.26

search(4)
Algorithm did not conclude running in a reasonable time frame.

Observations: Average depth increased significantly between search(2) and 
search(3), and likely between search(3) and search(4) which would explain why
the algorithm did not complete in reasonable time   
=============================
"""