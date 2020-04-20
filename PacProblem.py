'''
Project 1 - Search-based solutions for static Pac-Man game.

PacProblem.py: Basic problem type for Pac-Man problem.

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
from search import Problem

class PacProblem(Problem):
    ''' Modeling the static Pac-Man game problem for search. '''
    
    def __init__(self, initial, goal):
        ''' Initial State:
            Tuple of 2 elements. 1-Initial maze. 2. (i,j) in maze.
            Goal State:
            Tuple of 2 elements. (i,j) in maze.
        '''
        Problem.__init__(self, initial, goal)
        
    def actions(self, state):
        ''' A state is the current maze (NumPy 2D array) and the index of the maze (tuple). 
            An action is a tuple of i,j with the direction to walk.
        '''
        actions = []
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        maze,idx = state
        for action in possible:
            nxt = tuple(map(sum, zip(idx,action)))
            # TODO: circle around maze
            if maze[nxt] != 'O' and maze[nxt] != '|':
                actions.append(action)
        return actions

    def goal_test(self, state):
        ''' Check if the Pac-Man reaches its destination.'''
        return state[1] == self.goal

    def result(self, state, action):
        ''' The result of an action is to move to the next position, and eat the point if needed.'''
        maze, idx = state
        
        # Get next position.
        nxt = tuple(map(sum, zip(idx,action)))
        
        # Eat point if needed
        if maze[nxt] == '.': maze[nxt] = ' '
        return maze,nxt
    
    def path_cost(self, c, state1, action, state2):
        ''' 10 points if it eats a point, and minus 1 point per movement. '''
        if state1[0][state2[1]] == '.':
            cost = c-10
        else:
            cost = c
        return c+1

    def value(self, state):
        ''' Value is the "score" for the state.'''
        return -1 * self.path_cost(None, None, None, state)

