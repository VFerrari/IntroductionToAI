'''
Project 1 - Search-based solutions for static Pac-Man game.

Subject:
    MC906/MO416 - Introduction to Artificial Intelligence.
Authors:
    Daniel Helú Prestes de Oliveira - RA 166215
    Eduardo Barros Innarelli        - RA 170161
    Matheus Rotta Alves             - RA 184403
    Victor Ferreira Ferrari         - RA 187890
    Vinícius Couto Espindola        - RA 188115

University of Campinas - UNICAMP - 2020

Last Modified: 19/04/2020.
'''

import numpy as np
from search import Problem

class PacProblem(Problem):
    ''' Modeling the static Pac-Man game problem for search. '''
    
    def __init__(self, initial, goal, maze):
        Problem.__init__(self, initial, goal)
        
        # Maze is a NumPy array.
        self.maze = maze
        
    def actions(self, state):
        ''' A state is the index of the maze (tuple). 
            An action is a tuple of i,j such that result=state+action.
        '''
        actions = []
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        for action in possible:
            if self.maze[state[0]+action[0], state[1]+action[1]] == '.':
                actions.append(action)
        return actions

    def result(self, state, action):
        return tuple(map(sum, zip(state,action)))
