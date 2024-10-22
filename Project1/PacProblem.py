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

import numpy as np
from utils import manhattan_distance, euclidean_distance
from search import Problem

class PacProblem(Problem):
    ''' Modeling the static Pac-Man game problem for search. '''
    
    def __init__(self, initial, goal, heuristic = None):
        ''' Initial State:
            Tuple of 2 elements. 1-Initial maze. 2. (i,j) in maze.
            Goal State:
            Tuple of 2 elements. (i,j) in maze.
        '''
        Problem.__init__(self, initial, goal)
        self.visited = set()
        self.explored = set()
        self.repeated_states = 0
        self.counter = 0
        self.heuristic = heuristic
        self.current = [None,0]
        
    def actions(self, state):
        ''' 
            A state is the current maze (tuple of tuples) and the agent index
            in the maze (tuple). An action is a tuple of i,j with the direction 
            to walk.
        '''
        self.visited = self.visited.union([self.counter])

        actions = []
        possible = [(1,0),(-1,0),(0,1),(0,-1)]
        tuple_maze, idx = state
                
        # Convert maze into a numpy array.
        maze = np.array(tuple_maze)
        
        for action in possible:
            nxt = list(map(sum, zip(idx,action)))
                        
            # Check circling around maze. If < 0, negative indexing will do the job.
            if nxt[0] == maze.shape[0]:
                nxt[0] = 0
            elif nxt[0] < 0:
                nxt[0] = maze.shape[0]-1
            elif nxt[1] == maze.shape[1]:
                nxt[1] = 0
            elif nxt[1] < 0:
                nxt[1] = maze.shape[1] - 1
                
            nxt = tuple(nxt)
            
            # Check ghosts and walls.
            if maze[nxt] not in [b'o', b'|', b'-']:
                actions.append(action)
        
        self.explored = self.explored.union(range(self.counter,self.counter+4))
        self.counter += 4
        return actions

    def goal_test(self, state):
        ''' Check if the Pac-Man reaches its destination.'''
        return state[1] == self.goal

    def result(self, state, action):
        ''' The result of an action is to move to the next position, and eat the point if needed.'''
        tuple_maze, idx = state
        
        # Convert maze into a numpy array.         
        maze = np.array(tuple_maze)
        
        # Get next position.
        nxt = list(map(sum, zip(idx,action)))
        
        # Circle around maze.
        if nxt[0] == maze.shape[0]:
            nxt[0] = 0
        elif nxt[0] < 0:
            nxt[0] = maze.shape[0]-1
        elif nxt[1] == maze.shape[1]:
            nxt[1] = 0
        elif nxt[1] < 0:
            nxt[1] = maze.shape[1]-1
        
        nxt = tuple(nxt)
        
        # Eat point if needed
        if maze[nxt] == b'.':
            maze[nxt] = b' '
        return tuple(map(tuple, maze)), nxt
    
    def path_cost(self, c, state1, action, state2):
        ''' 10 points if it eats a point, and minus 1 point per movement. '''
        nxt = np.array(state1[0])[state2[1]]
        
        # Goal is same as a point (for now)
        if nxt == b'.' or nxt == b'?':
            cost = c-10
        else:
            cost = c
        return cost+1

    def value(self, state):
        ''' Value is the "score" for the state.'''
        ''' Value is the "score" for the state.'''
        # Use euclidean distance as a heuristic
        if self.heuristic == 'euclidean':
            return -5*euclidean_distance(state, self.goal)

        # Use manhatam distance as a heuristic
        if self.heuristic == 'manhattan':
            return -5*manhattan_distance(state, self.goal)

        # Use manhatam sum value as a heuristic
        if self.heuristic == 'pathcost':
            if state == self.current[0]:
                cost = self.current[1]
            elif self.maze[state] == b'.':
                cost = self.current[1] - 9
            else:
                cost = self.current[1] + 1
            return -1*cost

        # Error if no heuristic defined
        if not self.heuristic:
            raise Exception("CHOOSE A HEURISTIC before executing")
        if callable(self.heuristic):
            raise Exception("CHOOSE A HEURISTIC NAME before executing, not a function.")
    
    def h(self, node):
        ''' Heuristic for informed/local search methods '''
        
        assert self.heuristic != None, "Heuristic must be set!"
        
        # No need to receive maze to estimate, as it is stored in node.state
        return self.heuristic(node)

