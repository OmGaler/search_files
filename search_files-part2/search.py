#search
import state
import frontier

pushed = 0
popped = 0
moves = 0

def search(n):
    global pushed, popped, moves
    s=state.create(n)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            f[1] = len(s[-1]) #number of moves made 
            moves += f[1]
            pushed += f[3]
            popped += f[4]
            return [s, f[1]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0

size = 4
for i in range(100):
    answer = search(size)
    # print(answer)
print("%sx%s grid: " % (size, size)) 
print("Average moves: " + str(moves/100)) 
print("Average number pushed: " + str(pushed/100))
print("Average number popped: " + str(popped/100))


"""
=============================
OUTPUT
=============================
n=2

2x2 grid: 
Average moves: 1
Average number pushed: 2
Average number popped: 2

n=3

3x3 grid: 
Average moves: 5
Average number pushed: 18
Average number popped: 10

n=4

4x4 grid: 
Average moves: 15
Average number pushed: 584
Average number popped: 279
=============================
"""