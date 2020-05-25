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

Last Modified: 09/05/2020.
'''

import os, sys
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,f'{dir}/aima-python')

import numpy as np
from SearchAgent import SearchAgent
from sys import argv
from testing import run_tests, test_files
from wrapt_timeout_decorator import timeout

# Add aima folder to PYTHONPATH environment variable.
from search import greedy_best_first_graph_search, manhattan_distance, memoize
h_type = ''
def min_or_max_manhattan(node, maze = None):
    ''' minimum/maximum distance between the agent and a food '''
        
    assert h_type != '', 'Define a heuristic type (min or max)!'
        
    # Detach maze configuration (if in state) and Pac-Man position
    if not isinstance(maze, np.ndarray):
        tuple_maze, idx = node.state
    else:
        idx = node.state
        tuple_maze = None
    
    # Convert tuple maze into a numpy array
    maze = np.array(tuple_maze) if tuple_maze else maze
    
    # Take goal into account after a certain depth
    if node.depth < maze.shape[0]*maze.shape[1]*(3/4):
        foods_cond = maze == b'.'
    else:
        foods_cond = np.logical_or(maze == b'.', maze == b'?')
    
    # List all manhattan distances between the agent and the foods
    manhattan_distances = [
        manhattan_distance(food_idx, idx) 
        for food_idx 
        in np.argwhere(foods_cond)
    ]
    
    # If no more dots.
    if len(manhattan_distances) == 0:
        manhattan_distances = [
            manhattan_distance(food_idx, idx) 
            for food_idx 
            in np.argwhere(maze == b'?')
        ]
    
    # Get lowest/highest of them
    return min(manhattan_distances) if h_type == 'min' else max(manhattan_distances)
        
def gfs_pacman():
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
    agent.set_heuristic(manhattan_min)
    agent.search(greedy_best_first_graph_search_wrapper)
    actions = agent.get_solution()
    path = agent.transform_path()
    print('Actions (Graph): ', actions)
    print('Path (Graph): ', path) 
    print('Score (Graph): ', agent.get_score())
    
    # Apply actions in ascii.
    #sol = agent.apply_actions(actions)
    #np.savetxt('test.out', sol.astype('<U1'), delimiter=' ', fmt='%s')
    #print(sol.astype('<U1'))
    
    # Animate path
    agent.display_path(path, 0.2)

def gfs_tests():
    print(run_tests(test_files, gfs_pathcost_p2, [], out_path='data/gfs/problem2/max'))

def greedy_best_first_graph_search_wrapper(problem, h=None, display=False):
    h = memoize(h or problem.h, 'h')
    return greedy_best_first_graph_search(problem, lambda n: h(n), display)

#h_type = 'max'
def gfs_pathcost_p1(agent, maze, init, goal, *args):
    ''' triggers A* search and returns path cost '''
    agent.formulate_problem(init, goal, False, [b'-', b'|', b'o', b'_'])
    agent.set_heuristic(min_or_max_manhattan)
    agent.search(greedy_best_first_graph_search_wrapper)
    return agent.get_score()

h_type = 'max'
@timeout(30)
def gfs_pathcost_p2(agent, maze, init, goal, *args):
    ''' triggers A* search and returns path cost '''
    agent.formulate_problem(init, goal, True, [b'-', b'|', b'o', b'_'])
    agent.set_heuristic(min_or_max_manhattan)
    agent.search(greedy_best_first_graph_search_wrapper)
    return agent.get_score()

if __name__ == '__main__':
    #gfs_pacman()
    gfs_tests()
