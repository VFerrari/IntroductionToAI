import os
import numpy as np

def get_mazes():
  ''' Return mazes from './mazes' directory in a (denses, sparses) tuple '''

  # get maze file names as sorted integers (to facilitate analysis)

  denses_fn = sorted(
    [int(x) for x in os.listdir('./mazes/dense') if x.isdecimal()]
  )
  sparses_fn = sorted(
      [int(x) for x in os.listdir('./mazes/sparse') if x.isdecimal()]
  )

  # save them as numpy byte arrays (to save RAM)

  denses = [
      np.genfromtxt(
          './mazes/dense/' + str(dense), dtype='str', delimiter=1
      ).astype('bytes')
      for dense in denses_fn
  ]

  sparses = [
      np.genfromtxt(
          './mazes/sparse/' + str(sparse), dtype='str', delimiter=1
      ).astype('bytes')
      for sparse in sparses_fn
  ]

  return (denses, sparses)