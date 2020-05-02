import simulated_annealing as sa
import time, sys
from guppy import hpy
from itertools import product as combine

### THIS FUNCTION WAS TAKEN FROM https://gist.github.com/vladignatyev ###
def progress(count, total):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s\r' % (bar, percents, '%'))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)

# h = hpy()
# print(h.heap())

path = 'mazes/'
sizes = ['tiny/','medium/','big/']
files = ['1','2','3','4','5']
test_files = [path+s+f for (s,f) in list(combine(sizes,files))]


def test_annealing(test_files, repeat=20):
    for maze in test_files:
        print(f'\nRunning tests on {maze}\n')
        deltas = []
        fails = []
        costs = []
        best_path = None

        for i in range(1,repeat+1):
            progress(i, repeat)
            
            # Run and time it
            t0 = time.perf_counter()
            best_path = sa.sa_pacman(maze)      
            tf = time.perf_counter()

            # Data acumulators
            deltas += [tf - t0]
            fails += [0 if best_path else 1]
            costs += [0 if not best_path else best_path[1]]
        print('\n\n')

        if sum(fails)==repeat :
            print(f'COMPLETE FAILURE: not a single run (out of {repeat}) was able to reach the goal.')
            continue

        print(f'Stats for {maze}:')
        print(f'  Failed {sum(fails)} out of {repeat}')
        print(f'  Time Data:')
        print(f'    Avg (with fails): {sum(deltas)/repeat:.3f}')
        print(f'  Cost Data:')
        print(f'    Avg (no fails): {sum(costs)/(repeat-sum(fails)):.3f}')
        
test_annealing(test_files, repeat=1000)
