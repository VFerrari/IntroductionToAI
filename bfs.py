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

Last Modified: 07/05/2020.
'''

import os, sys
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,f'{dir}/../aima')

import numpy as np
from SearchAgent import SearchAgent
from sys import argv
from testing import run_tests, test_files

# Add aima folder to PYTHONPATH environment variable.
from search import breadth_first_tree_search, breadth_first_graph_search

def bfs_pacman():
    maze = np.array([['|', '|', '|', '|', '|'],
                    ['|', '.', '.', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['.', '.', '|', '.', '.'],
                    ['|', '.', '.', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '!', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '?', '|'],
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
                    ['|', '.', '|', '.', '|'],
                    ['|', '.', '|', '.', '|'],
                    ['|', '|', '|', '|', '|']]).astype('bytes')

    # Get maze from file
    # Careful: can use a lot of RAM if Problem2
    if len(argv) > 1:
        maze = np.genfromtxt(argv[1], dtype=str, delimiter=1).astype('bytes')
    
    # Create Agent
    agent = SearchAgent(maze)
    
    # Find initial and goal positions
    init, goal = agent.find_positions()
    init = (2,1) if not init else init
    goal = (15,3) if not goal else goal
    
    # Create Problem
    agent.formulate_problem(init, goal, False, False, [b'-', b'|', b'o', b'_'])
    
    # Solve with BFS
    # Problem: explodes too fast 
    #agent.search(breadth_first_tree_search)
    print('Actions (Tree): ', agent.get_solution())
    print('Score (Tree): ', agent.get_score())
    
    # Graph: Only works without maze in state.
    agent.search(breadth_first_graph_search)
    actions = agent.get_solution()
    path = agent.transform_path()
    print('Actions (Graph): ', actions)
    print('Path (Graph): ', path) 
    print('Score (Graph): ', agent.get_score())
    
    # Apply actions in ascii.
    sol = agent.apply_actions(actions)
    np.savetxt('test.out', sol.astype('<U1'), delimiter=' ', fmt='%s')
    print(sol.astype('<U1'))
    
    # Animate path
    agent.display_path(path, 0.3)

def bfs_tests():
    print(run_tests(test_files, bfs_pathcost, [], out_path='data/bfs/problem1'))

def bfs_pathcost(agent, maze, init, goal, *args):
    agent.formulate_problem(init, goal, False, False, [b'-', b'|', b'o', b'_'])
    agent.search(breadth_first_graph_search)
    return agent.get_score()

if __name__ == '__main__':
    #bfs_pacman()
    bfs_tests()
