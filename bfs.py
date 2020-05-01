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

Last Modified: 01/05/2020.
'''

import numpy as np
from PacProblemNoMaze import PacProblem
from SearchAgent import SearchAgent
from sys import argv

# Add aima folder to PYTHONPATH environment variable.
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
    if len(argv) > 1:
        maze = np.genfromtxt(argv[1], dtype=str, delimiter=1).astype('bytes')
    
    # Create Agent
    agent = SearchAgent(maze)
    
    # Create Problem
    init = (5,1)
    goal = (15,3)
    agent.formulate_problem(init, goal, [b'-', b'|', b'o', b'_'])
    
    # Solve with BFS
    # Problem: explodes too fast 
    agent.search(breadth_first_tree_search)
    print('Actions (Tree): ', agent.get_solution())
    print('Score (Tree): ', agent.get_score())
    
    # Graph: Only works without maze in state.
    agent.search(breadth_first_graph_search)
    actions = agent.get_solution()
    print('Actions (Graph): ', actions)
    print('Score (Graph): ', agent.get_score())
    
    sol = agent.apply_actions(actions)
    np.savetxt('test.out', sol.astype('<U1'), delimiter=' ', fmt='%s')
    print(sol.astype('<U1'))

if __name__ == '__main__':
    bfs_pacman()
