'''
Project 1 - Search-based solutions for static Pac-Man game.

SearchAgent.py: Generic search agent.

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

import numpy as np
from PacProblemNoMaze import PacProblem as Problem1
from PacProblem import PacProblem as Problem2
from PacScreen import PacScreen

class SearchAgent:
    def __init__(self, maze):
        self.maze = maze
        self.display = None
        self.problem = None
        self.solution = None
        self.init = None
        self.state_maze = False
        self.heuristic = None
    
    def set_maze(self, maze):
        self.maze = maze
        if self.problem and not self.state_maze:
            self.problem.maze = maze.copy()
            
    def set_heuristic(self, heuristic):
        self.heuristic = heuristic
        if self.problem:
            self.problem.heuristic = heuristic

    def find_positions(self):
        ''' Find initial and goal positions in correctly made mazes.'''
        init = np.where(self.maze == b'!')
        goal = np.where(self.maze == b'?')

        # If init is not defined.
        if init[0].size == 0:
            init = None
        else:
            init = init[0][0], init[1][0]
        
        # If goal is not defined.
        if goal[0].size == 0:
            goal = None
        else:
            goal = goal[0][0], goal[1][0]
        return init, goal
    
    def formulate_problem(self, initial_pos, goal_pos, with_maze, goal_conditions):
        ''' Formulates problem based on positions and if maze is in state or not.'''
        self.init = initial_pos        
        
        # Conditions
        assert all(self.maze[initial_pos] != t for t in goal_conditions), "Initial position does not satisfy conditions!"
        assert all(self.maze[goal_pos] != t for t in goal_conditions), "Goal does not satisfy conditions!"
    
        if not with_maze:
            # Problem with maze in state
            self.problem = Problem1(initial_pos, goal_pos, self.maze.copy(), self.heuristic)
        else:
            # Problem with only Pac-Man position in state
            initial_pos = (tuple(map(tuple, self.maze)), initial_pos)
            self.problem = Problem2(initial_pos, goal_pos, self.heuristic)
        
        self.state_maze = with_maze
                                                  
    def search(self, method, *args):
        ''' Execute search (solve problem). '''
        self.solution = method(self.problem, *args)
    
    def get_solution(self):
        if isinstance(self.solution, tuple):
            return self.solution
        elif self.solution:
            return self.solution.solution()
        else:
            return []
    
    def get_path(self):
        if self.solution:
            return self.solution.path()
        else:
            return []
            
    def get_score(self):
        if self.solution:
            return -1*self.solution.path_cost
        else:
            return 0
    
    def get_explored(self):
        if self.problem:
            return len(self.problem.explored)
        else: 
            return None

    def get_visited(self):
        if self.problem:
            return len(self.problem.visited)
        else: 
            return None

    def get_repeated(self):
        if self.problem:
            return self.problem.repeated_states
        else: 
            return None


    def transform_path(self):
        ''' Transforms a path of nodes to a path of positions. '''
        pos = []
        path = self.solution.path()
        
        # Transform to positions            
        # If maze is in state
        if self.state_maze:
            for node in path:
                pos.append(node.state[1])
        else:
            for node in path:
                pos.append(node.state)
        return pos
    
    def display_path(self, path, interval=0.005):
        ''' Animate maze, to visualize found path. '''
        self.display = PacScreen(self.maze)
        self.display.run(path, interval)
    
    def apply_actions(self, actions):
        ''' Apply actions to maze in ascii, to visualize found path. '''
        direct_x = {1:b'>', -1:b'<'}
        direct_y = {-1:b'^', 1:b'v'}
        directions = {b'^', b'v', b'<', b'>'}
        maze = self.maze.copy()
        pos = self.init
        
        # Initial
        maze[pos] = b'!'
        for act in actions:
            pos = list(map(sum, zip(pos,act)))
            
            # Circle around maze
            if pos[0] == maze.shape[0]:
                pos[0] = 0
            elif pos[0] < 0:
                pos[0] = maze.shape[0]-1
            elif pos[1] == maze.shape[1]:
                pos[1] = 0
            elif pos[1] < 0:
                pos[1] = maze.shape[1]-1
            pos = tuple(pos)
            
            if maze[pos] in directions:
                continue
            
            if act[0] != 0:
                maze[pos] = direct_y[act[0]]
            elif act[1] != 0:      
                maze[pos] = direct_x[act[1]]
        
        # Goal
        maze[pos] = b'?'
        return maze
