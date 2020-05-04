import os
import numpy as np

def gen_sparses(dir_path):
  ''' Randomly remove points from dense instances '''

  denses = sorted([int(x) for x in os.listdir(dir_path + '/dense') if x.isdecimal()])

  for idx, dense in enumerate(denses):
      sparse = np.genfromtxt(dir_path + '/dense/' + str(idx + 1), dtype='str', delimiter=1)
          
      for r in range(0, len(sparse)):
          for c in range(0, len(sparse[0])):
              if sparse[r][c] == '.':
                  sparse[r][c] = ' ' if bool(np.random.choice(np.arange(0,2), p=[0.25,0.75])) else '.'
              
      np.savetxt(dir_path + '/sparse/' + str(idx + 1), sparse, fmt='%s', delimiter='')