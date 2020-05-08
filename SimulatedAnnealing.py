'''
Project 1 - Search-based solutions for static Pac-Man game.

sa.py: Simulated Annealing search solutions for problem.

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

# This block will allow relative imports from the AIMA folder
# Call it before any other import
import os, sys
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,f'{dir}/aima-python')

from numpy import exp, genfromtxt
from SearchAgent import SearchAgent
from search import simulated_annealing_full

def get_best_path(states, maze, goal):
        ''' Calculate the cost after getting a path from some search method. '''
        min_idx = None 
        min_cost = sys.maxsize
        cost = 0

        for i,pos in enumerate(states):        
            if maze[pos] == b'.':
                cost -= 9 # Reduce cost by 10 and add 1
                maze[pos] = b' ' # Eat pos
            else:
                cost += 1

            # Check if at a goal state with a better cost
            if pos == goal and cost < min_cost:
                min_cost = cost
                min_idx = i

        # Check if reached the goal state at all
        if min_idx:
            path = states[:min_idx+1]
            return (path, min_cost)
        else: 
            return (states, None)

# Cooler for pathcost heuristic
def pathcost_cooler(k=5, lam=0.0003, limit=2000):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * exp(-lam * t) if t < limit else 0)

def annealing(problem, maze, goal):
    # Copy for post processing
    maze_ref = maze.copy()

    # Solve with Simulated Annealing
    states = simulated_annealing_full(problem, schedule=pathcost_cooler())

    # Get the best path found
    best = get_best_path(states, maze_ref, goal)
    
    return best    


from itertools import product as combine
from random import choice

if __name__ == '__main__':
    
    # Getting test files
    path = 'mazes/'
    sizes = ['dense/','sparse/']
    maze = ['1','2','3','4','5','6','7','8','9','10']
    pos = ['a','b','c']
    test_files = [path+s+i+l for (s,i,l) in list(combine(sizes,maze,pos))]

    while True:
        # Simulated Annealing Sample
        maze_file = choice(test_files)
        maze = genfromtxt(maze_file, dtype=str, delimiter=1).astype('bytes')
        agent = SearchAgent(maze)
        init,goal = agent.find_positions()
        agent.formulate_problem(init, goal, False, [])
        agent.search(annealing, maze, goal)
        path = agent.get_solution()[0]
        agent.display_path(path)
