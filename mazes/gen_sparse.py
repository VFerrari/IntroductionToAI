import glob
import numpy as np

dense_path = './dense/'
sparse_path = './sparse/'

def gen_sparse():
  ''' Randomly remove points from dense instances '''

  denses = [test for test in glob.glob(dense_path + '*')]

  for idx, dense in enumerate(denses):
      sparse = np.genfromtxt(dense, dtype='str', delimiter=1)
          
      for r in range(0, len(sparse)):
          for c in range(0, len(sparse[0])):
              if sparse[r][c] == '.':
                  sparse[r][c] = ' ' if bool(np.random.choice(np.arange(0,2), p=[0.25,0.75])) else '.'
              
      np.savetxt('./sparse/' + str(idx + 1), sparse, fmt='%s', delimiter='')

gen_sparse()