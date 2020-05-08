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

Last Modified: 03/05/2020.
'''

# This block will allow relative imports from the AIMA folder
# Call it before any other import
import os, sys
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,f'{dir}/aima-python')

from search import Problem
from numpy import sqrt

choose_dist = 'euclidean'

class PacProblem(Problem):
    ''' Modeling the static Pac-Man game problem for search. '''
    
    def __init__(self, initial, goal, maze):
        ''' Initial State:
            Tuple of 2 elements. (i,j) in maze.
            Goal State:
            Tuple of 2 elements. (i,j) in maze.
            Maze:
            NumPy array of BYTES (to save RAM)
        '''
        Problem.__init__(self, initial, goal)
        self.maze = maze
        
    def actions(self, state):
        ''' A state is the index of the maze (tuple). 
            An action is a tuple of i,j with the direction to walk.
        '''
        actions = []
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        idx = state

        # This is the new behavior of eating the points
        # Eat point if needed
        if self.maze[idx] == b'.':
            self.maze[idx] = b' '
        for action in possible:
            nxt = list(map(sum, zip(idx,action)))
            
            # Check circling around maze. If < 0, negative indexing will do the job.
            if nxt[0] == self.maze.shape[0]:
                nxt[0] = 0
            elif nxt[1] == self.maze.shape[1]:
                nxt[1] = 0
            nxt = tuple(nxt)
            
            # Check ghosts and walls.
            if self.maze[nxt] not in [b'o', b'|', b'-']:
                actions.append(action)
        return actions

    def goal_test(self, state):
        ''' Check if the Pac-Man reaches its destination.'''
        return state == self.goal

    def result(self, state, action):
        ''' The result of an action is to move to the next position, and eat the point if needed.'''
        idx = state
        
        # Get next position.
        nxt = list(map(sum, zip(idx,action)))
        
        # Circle around maze.
        if nxt[0] == self.maze.shape[0]:
            nxt[0] = 0
        elif nxt[0] < 0:
            nxt[0] = self.maze.shape[0]-1
        elif nxt[1] == self.maze.shape[1]:
            nxt[1] = 0
        elif nxt[1] < 0:
            nxt[1] = self.maze.shape[1]-1
        
        nxt = tuple(nxt)
        
        # This is the old behavior of eating the points
        # Eat point if needed
        # if self.maze[nxt] == b'.':
        #     self.maze[nxt] = b' '
        return nxt
    
    def path_cost(self, c, state1, action, state2):
        ''' 10 points if it eats a point, and minus 1 point per movement. '''
        nxt = self.maze[state2]
        # Goal is same as a point (for now)
        if nxt == b'.' or nxt == b'?':
            cost = c-10
        else:
            cost = c
        return cost+1

    def value(self, state):
        ''' Value is the "score" for the state.'''
        # Use euclidean distance as a heuristic
        if choose_dist == 'euclidean':
            Ax,Ay = state
            Bx,By = self.goal
            return -5*sqrt((Ax-Bx)**2 + (Ay-By)**2)

        # Use manhatam distance as a heuristic
        if choose_dist == 'manhatam':
            Ax,Ay = state
            Bx,By = self.goal
            return -5*(abs(Ax-Bx) + abs(Ay-By))
