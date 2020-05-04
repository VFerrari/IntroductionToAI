import simulated_annealing as sa
import time, sys, re
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

# Getting test files
path = 'mazes/'
sizes = ['classicsA/','classicsB/']
files = ['1','2','3','4','5']
test_files = [path+s+f for (s,f) in list(combine(sizes,files))]


def test_annealing(test_files, repeat=20, fill=False):
    general = dict()
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
            best_path = sa.sa_pacman(maze, fill=fill)      
            tf = time.perf_counter()

            # Data acumulators
            deltas += [tf - t0]
            fails += [0 if best_path else 1]
            costs += [0 if not best_path else best_path[1]]
        print('\n\n')

        total_fails = sum(fails)
        deltas_avg = sum(deltas)/repeat # Consider failures
        if total_fails != repeat:
            cost_avg = sum(costs)/(repeat-sum(fails)) # Don't consider failures
        else:
            cost_avg = 0
        
        general[maze] = (total_fails, deltas_avg, cost_avg)
        
        if sum(fails)==repeat :
            print(f'COMPLETE FAILURE: not a single run (out of {repeat}) was able to reach the goal.')
            continue

        print(f'Stats for {maze}:')
        print(f'  Failed {total_fails} out of {repeat}')
        print(f'  Time Data:')
        print(f'    Avg (with fails): {deltas_avg:.3f}')
        print(f'  Cost Data:')
        print(f'    Avg (no fails): {cost_avg:.3f}')

    stats = {'classicsA':(0,0,0,0),'classicsB':(0,0,0,0)}#{'tiny':(0,0,0,0),'medium':(0,0,0,0),'big':(0,0,0,0)}
    for name,(f,d,c) in zip(general.keys(),general.values()):
        size = re.match(r'mazes/(.+)/.+', name).group(1)
        (w,x,y,z) = stats[size]
        stats[size] = (w+repeat,x+f,y+d,z+c)

    print(f'\n')
    print(f'GENERAL STATS:')
    for key in stats.keys():
        (r,f,d,c) = stats[key]
        qnt_files = (r/repeat) 
        print(f'  {key}:')
        print(f'    fails - {f}/{r}')
        print(f'    time - {d/qnt_files:.3f}')
        print(f'    cost - {c/qnt_files:.3f}')
        
test_annealing(test_files, repeat=100, fill=True)
