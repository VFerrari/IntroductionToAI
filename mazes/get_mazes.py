import os
import re
import numpy as np

def get_mazes():
  ''' 
  Return mazes from './mazes' directory as numpy byte arrays in a (denses, 
  sparses) tuple
  '''

  pattern = re.compile('^([0-9]+[a-zA-Z]+)')

  denses = [
      np.genfromtxt(
          './mazes/dense/' + str(dense), dtype='str', delimiter=1
      ).astype('bytes')
      # Get file name
      for dense 
      in os.listdir('./mazes/dense') 
      if pattern.match(dense)
  ]

  sparses = [
      np.genfromtxt(
          './mazes/sparse/' + str(sparse), dtype='str', delimiter=1
      ).astype('bytes')
      # Get file name
      for sparse 
      in os.listdir('./mazes/sparse') 
      if pattern.match(sparse)
  ]

  return (denses, sparses)