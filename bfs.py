'''
Project 1 - Search-based solutions for static Pac-Man game.

bfs.py: breadth-first search solutions for problem.

Subject:
    MC906/MO416 - Introduction to Artificial Intelligence.
Authors:
    Daniel Helú Prestes de Oliveira - RA 166215
    Eduardo Barros Innarelli        - RA 170161
    Matheus Rotta Alves             - RA 184403
    Victor Ferreira Ferrari         - RA 187890
    Vinícius Couto Espindola        - RA 188115

University of Campinas - UNICAMP - 2020

Last Modified: 20/04/2020.
'''

import numpy as np
import sys

# REMOVE (path)
sys.path.insert(0, '../aima-python')

from PacProblem import PacProblem
from search import breadth_first_tree_search, breadth_first_graph_search

def bfs_pacman():
    maze = np.array([['|', '|', '|', '|', '|'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['.', '.', '|', '.', '.'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '|', '|', '|', '|']]).astype('bytes')

    # Get maze from file
    # Careful: uses a lot of RAM
    #maze = np.genfromtxt('test', dtype=str, delimiter=1).astype('bytes')
    
    # Create Problem
    init = (maze, (1,1))
    goal = (15,3)
    prob = PacProblem(init, goal)
    assert maze[goal] == b'.' or maze[goal] == b' ', "Goal unreachable."
    
    # Solve with BFS
    # Problem: explodes too fast 
    # Test 1: 15 lines of the above maze: 28 seconds and 500MB RAM.
    # Test 2: 16 lines of the above maze: 61 seconds and 1.3GB RAM. (exponential behavior)
    final_state = breadth_first_tree_search(prob)
    print('Actions (Tree): ', final_state.solution())
    print('Score (Tree): ', -1*final_state.path_cost)
    
    # Graph: not working because numpy array is not hashable.
    #final_state = breadth_first_graph_search(prob)
    #print('Actions (Graph): ', final_state.solution())

if __name__ == '__main__':
    bfs_pacman()
