import os
import re
import numpy as np

# WARNING: this function overrides the mazes in sparse directory; don't run it
# as the idea is that everyone test the same mazes

def gen_sparses(dir_path):
  ''' Randomly remove points from dense instances '''

  pattern = re.compile('^([0-9]+[a-zA-Z]+)')
  denses_fn = [x for x in os.listdir(dir_path + '/dense') if pattern.match(x)]

  print(denses_fn)
  for dense_fn in denses_fn:
      sparse = np.genfromtxt(dir_path + '/dense/' + dense_fn, dtype='str', delimiter=1)
          
      for r in range(0, len(sparse)):
          for c in range(0, len(sparse[0])):
              if sparse[r][c] == '.':
                  sparse[r][c] = ' ' if bool(np.random.choice(np.arange(0,2), p=[0.25,0.75])) else '.'
              
      np.savetxt(dir_path + '/sparse/' + dense_fn, sparse, fmt='%s', delimiter='')

gen_sparses('.')