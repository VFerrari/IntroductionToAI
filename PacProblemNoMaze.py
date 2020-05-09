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

Last Modified: 09/05/2020.
'''

# This block will allow relative imports from the AIMA folder
# Call it before any other import
import os, sys
dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,f'{dir}/aima-python')

from search import Problem
from utils import manhattan_distance, euclidean_distance
import numpy as np

class PacProblem(Problem):
    ''' Modeling the static Pac-Man game problem for search. '''
    
    def __init__(self, initial, goal, maze, heuristic = None):
        ''' Initial State:
            Tuple of 2 elements. (i,j) in maze.
            Goal State:
            Tuple of 2 elements. (i,j) in maze.
            Maze:
            NumPy array of BYTES (to save RAM)
        '''
        Problem.__init__(self, initial, goal)
        self.maze = maze
        self.heuristic = heuristic
        self.visited = set()
        self.explored = set()
        self.repeated_states = 0
        
    def actions(self, state):
        ''' A state is the index of the maze (tuple). 
            An action is a tuple of i,j with the direction to walk.
        '''
        if state[0]*100+state[1] in self.visited: 
            self.repeated_states += 1
        self.visited = self.visited.union([state[0]*100+state[1]])
        
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
        self.explored = self.explored.union([nxt[0]*100+nxt[1]])

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
        if self.heuristic == 'euclidean':
            return -5*euclidean_distance(state, self.goal)

        # Use manhatam distance as a heuristic
        if self.heuristic == 'manhattan':
            return -5*manhattan_distance(state, self.goal)

        # Use manhatam sum value as a heuristic
        if self.heuristic == 'manhattan_sum':
            # Accumulate sum of manhattan distances to foods
            md_sum = 0
            for food_idx in np.argwhere(self.maze == '.'):
                md_sum += manhattan_distance(food_idx, state)
            
            tenth = len(np.argwhere(self.maze == ''))*0.1
            goal_dist = -1*tenth*manhattan_distance(state, self.goal)
            
            return md_sum + goal_dist

        # Error if no heuristic defined
        if not self.heuristic:
            raise Exception("CHOOSE A HEURISTIC before executing")
        if callable(self.heuristic):
            raise Exception("CHOOSE A HEURISTIC NAME before executing, not a function.")
        
    def h(self, node):
        ''' Heuristic for informed/local search methods '''
        
        assert self.heuristic != None, "Heuristic must be set!"
        assert callable(self.heuristic), "Heuristic must be a function!"
        
        # Need to receive maze to estimate
        return self.heuristic(node, self.maze)
