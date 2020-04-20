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
        # I think this maze has to be part of the state.
        self.maze = maze
        
    def actions(self, state):
        ''' A state is the index of the maze (tuple). 
            An action is a tuple of i,j such that result=state+action.
        '''
        actions = []
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        for action in possible:
            nxt = (state[0]+action[0], state[1]+action[1])
            if self.maze[nxt] != 'O' and self.maze[nxt] != '|':
                actions.append(action)
        return actions

    def result(self, state, action):
        return tuple(map(sum, zip(state,action)))
    
    def path_cost(self, c, state1, action, state2):
        ''' 10 points if it eats a point, and minus 1 point per movement. '''
        if self.maze[state2] == '.':
            cost = c-10
        else:
            cost = c
        return c+1
