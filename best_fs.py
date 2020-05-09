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
sys.path.insert(0,f'{dir}/aima-python')

import numpy as np
from SearchAgent import SearchAgent
from sys import argv
from testing import run_tests, test_files

# Add aima folder to PYTHONPATH environment variable.
from search import greedy_best_first_graph_search, recursive_best_first_search, manhattan_distance
from utils import memoize

# Heuristic for problem 1 - without maze in state
def astar_heuristic_p1(node, goal):
    ''' manhattan distance between Pac-Man and goal '''
    
    idx = node.state
    md = manhattan_distance(goal, idx)
    return md

# Heuristic for problem 2 - with maze in state
def astar_heuristic_p2(node):
    ''' sum of manhattan distances between Pac-Man and all foods in maze '''
    
    # Detach maze configuration and Pac-Man position
    tuple_maze, idx = node.state
    maze = np.array(tuple_maze)
    
    # Accumulate sum of manhattan distances to foods
    md_sum = 0
    for food_idx in np.argwhere(maze == '.'):
        md_sum += manhattan_distance(food_idx, idx)
            
    return md_sum

def best_fs_pacman():
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
    agent.formulate_problem(init, goal, True, [b'-', b'|', b'o', b'_'])
    
    # Graph: Only works without maze in state.
    agent.set_heuristic(astar_heuristic_p2, False)
    agent.search(greedy_best_first_graph_search_wrapper)
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

def best_fs_tests():
    print(run_tests(test_files, best_fs_pathcost_p1, [], out_path='data/best_fs/problem1'))

def greedy_best_first_graph_search_wrapper(problem, h=None, display=False):
    h = memoize(h or problem.h, 'h')
    return greedy_best_first_graph_search(problem, lambda n: h(n), display)

def best_fs_pathcost_p1(agent, maze, init, goal, *args):
    ''' triggers A* search and returns path cost '''
    agent.formulate_problem(init, goal, False, [b'-', b'|', b'o', b'_'])
    agent.set_heuristic(astar_heuristic_p1, True)
    agent.search(greedy_best_first_graph_search_wrapper)
    return agent.get_score()

def best_fs_pathcost_p2(agent, maze, init, goal, *args):
    ''' triggers A* search and returns path cost '''
    agent.formulate_problem(init, goal, True, [b'-', b'|', b'o', b'_'])
    agent.set_heuristic(astar_heuristic_p2, False)
    agent.search(greedy_best_first_graph_search_wrapper)
    return agent.get_score()

if __name__ == '__main__':
    best_fs_pacman()
    #best_fs_tests()
