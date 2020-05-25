'''
Project 1 - Search-based solutions for static Pac-Man game.

dfs.py: depth-first search solutions for problem.

Subject:
    MC906/MO416 - Introduction to Artificial Intelligence.
Authors:
    Daniel Helú Prestes de Oliveira - RA 166215
    Eduardo Barros Innarelli        - RA 170161
    Matheus Rotta Alves             - RA 184403
    Victor Ferreira Ferrari         - RA 187890
    Vinícius Couto Espindola        - RA 188115

University of Campinas - UNICAMP - 2020
'''

import numpy as np
from SearchAgent import SearchAgent
from sys import argv

from search import depth_first_graph_search

def dfs_pacman():
    maze = np.array([['|', '|', '|', '|', '|'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['.', '.', '|', '.', '.'],
                ['|', '.', '.', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '!', '|', '.', '|'],
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
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '.', '|', '.', '|'],
                ['|', '|', '|', '|', '|']]).astype('bytes')

    # Get maze from file

    if len(argv) > 1:
        maze = np.genfromtxt(argv[1], dtype=str, delimiter=1).astype('bytes')
        
    # Create Agent
    agent = SearchAgent(maze)
    

    init, goal = agent.find_positions()


    # Create Problem
    agent.formulate_problem(init, goal, False, False, [b'-', b'|', b'o', b'_'])
    
    # Graph: Only works without maze in state.
    agent.search(depth_first_graph_search)
    actions = agent.get_solution()
    if len(actions) == 0:
        print("It's not possible to get to the goal")
    else:
        path = agent.transform_path()
        print('Actions (Graph): ', actions)
        print('Path (Graph): ', path)
        print('Score (Graph): ', agent.get_score())

        # sol = agent.apply_actions(actions)
        # np.savetxt('test.out', sol.astype('<U1'), delimiter=' ', fmt='%s')
        # print(sol.astype('<U1'))

        agent.display_path(path, 0.3)

if __name__ == '__main__':
    dfs_pacman()
