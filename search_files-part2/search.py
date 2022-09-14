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
            popped += f[4]
            pushed += f[3]
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
print("Average solution path cost: " + str(moves/100.0)) 
print("Average number pushed: " + str(pushed/100.0))
print("Average number popped: " + str(popped/100.0))

"""
=============================
OUTPUT
=============================


===========
Unweighted A*
===========

search(4), using heuristic hdistance1 (number of tiles out of place)
4x4 grid: 
Average solution path cost: 13.6
Average number pushed: 25702.2
Average number popped: 12174.8

search(4), using heuristic hdistance2 (manhattan distance)
4x4 grid: 
Average solution path cost: 15.75
Average number pushed: 977.96
Average number popped: 465.93

===========
Weighted A*
===========

search(4), using heuristic 2hdistance1 (number of tiles out of place)
4x4 grid: 
Average solution path cost: 18.1
Average number pushed: 10385.4
Average number popped: 4775.2

search(4), using heuristic 2hdistance2 (manhattan distance)
4x4 grid: 
Average solution path cost: 16.89
Average number pushed: 601.78
Average number popped: 282.59

Observations: running the weighted A* search generally gave a greater average solution 
cost (optimality/path length) compared to unweighted A* but significantly reduces 
the runtime and number of states checked
=============================

"""