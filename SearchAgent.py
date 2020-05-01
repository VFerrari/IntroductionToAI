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

Last Modified: 01/05/2020.
'''

from PacProblemNoMaze import PacProblem

class SearchAgent:
    def __init__(self, maze):
        self.maze = maze
        self.problem = None
        self.solution = None
    
    def set_maze(self, maze):
        self.maze = maze
        if self.problem:
            self.problem.maze = maze.copy()
        
    def formulate_problem(self, initial_pos, goal_pos, goal_conditions):
        assert all(self.maze[goal_pos] != t for t in goal_conditions), "Goal does not satisfy conditions!"
        
        self.problem = PacProblem(initial_pos, goal_pos, self.maze.copy())
    
    def search(self, method):
        self.solution = method(self.problem)
    
    def get_solution(self):
        if self.solution:
            return self.solution.solution()
        else:
            return []
    
    def get_score(self):
        if self.solution:
            return -1*self.solution.path_cost
        else:
            return 0        
    
    def apply_actions(self, actions):
        raise NotImplementedError
