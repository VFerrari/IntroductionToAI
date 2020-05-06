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

from numpy import exp
from search import simulated_annealing_full

# NOTE: It assumes the state contains it's respective score
def get_best_path(states, maze, goal):
        ''' Calculate the cost after getting a path from some search method. '''
        min_idx = None 
        min_cost = sys.maxsize

        for i,(p,c) in enumerate(states):        
            # Check if at a goal state with a better cost
            if p == goal and c < min_cost:
                min_cost = c
                min_idx = i

        # Check it reached the goal state at all
        if min_idx: 
            path = [states[i][0] for i in range(min_idx+1)]
            return True, (path, min_cost)
        else: 
            path = [s[0] for s in states]
            return False, (path, None)

def cooling_func(k=10, lam=0.001, limit=2000):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * exp(-lam * t) if t < limit else 0)

def execute(problem, maze, init, goal, wrong_path=False):
    # Copy for post processing
    maze_ref = maze.copy()

    # Solve with Simulated Annealing
    states = simulated_annealing_full(problem, schedule=cooling_func())

    # Get the best path found
    reached,best = get_best_path(states, maze_ref, goal)
    if not reached: print("The search failed to reach a final state.")
    
    return best    
    