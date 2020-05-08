'''
Project 1 - Search-based solutions for static Pac-Man game.

draw.py: Animate Pac-Man path.

Subject:
    MC906/MO416 - Introduction to Artificial Intelligence.
Authors:
    Daniel Helú Prestes de Oliveira - RA 166215
    Eduardo Barros Innarelli        - RA 170161
    Matheus Rotta Alves             - RA 184403
    Victor Ferreira Ferrari         - RA 187890
    Vinícius Couto Espindola        - RA 188115

University of Campinas - UNICAMP - 2020

Last Modified: 05/05/2020.
'''

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as py
import numpy as np
#import simulated_annealing as sa
from time import sleep

black = (0,0,0)
grey = (50,50,50)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,200)
yellow = (255,255,0)

# Múltiple of 4 ples
px = 28

class PacScreen():

    def __init__(self, maze):
        self.maze = maze.copy()
        self.size = (self.maze.shape[1]*px,self.maze.shape[0]*px)

        self.pac = tuple(map(int, np.where(self.maze==b'!')))
        self.goal = tuple(map(int, np.where(self.maze==b'?'))) 

    def draw(self, maze, pac, goal):
        walls = (maze==b'|')
        bars = (maze==b'-')
        dots = (maze==b'.')
        ghosts = (maze==b'o')
        y_max,x_max = maze.shape

        for i in range(y_max):
            for j in range(x_max):
                x = j*px
                y = i*px
                if walls[i][j]:
                    py.draw.rect(self.disp, blue, (x,y,px,px))
                if bars[i][j]:
                    py.draw.rect(self.disp, white, (x,int(y+px/2-px/4),px,int(px/4)))
                if dots[i][j]:
                    x_c = int(x+px/2)
                    y_c = int(y+px/2)
                    rad = int(px/5)
                    py.draw.circle(self.disp, white, (x_c,y_c), rad)
                if ghosts[i][j]:
                    a = (x,y+px)
                    b = (x+px,y+px)
                    c = (int(x+px/2),y)
                    py.draw.polygon(self.disp, green, (a,b,c))
        
        x_c = int(pac[1]*px + px/2)
        y_c = int(pac[0]*px + px/2)
        rad = int(px/3)
        py.draw.circle(self.disp, yellow, (x_c,y_c), rad)

        x_c = int(goal[1]*px + px/2)
        y_c = int(goal[0]*px + px/2)
        rad = int(px/4)
        py.draw.circle(self.disp, red, (x_c,y_c), rad)

    def update(self, maze, pac):
        # Erase old pacman
        x = self.pac[1]*px
        y = self.pac[0]*px
        py.draw.rect(self.disp, black, (x,y,px,px))
        
        # Leave visited tag
        x_c = int(self.pac[1]*px + px/2)
        y_c = int(self.pac[0]*px + px/2)
        rad = int(px/4)
        py.draw.circle(self.disp, grey, (x_c,y_c), rad)

        # Update and draw
        self.pac = pac
        x_c = int(self.pac[1]*px + px/2)
        y_c = int(self.pac[0]*px + px/2)
        rad = int(px/3)
        py.draw.circle(self.disp, yellow, (x_c,y_c), rad)

    def step(self, action):    
        if self.maze[action] == b'.':
            self.maze[action] = ' ' 
        self.update(self.maze, action)

    def run(self, path, interval=0.005):
        # Create window and draw
        self.disp = py.display.set_mode(self.size)
        self.disp.fill(black)
        self.map = py.PixelArray(self.disp)
        self.draw(self.maze, self.pac, self.goal)

        # Animate
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    return

            if path:
                self.step(path.pop(0))
                py.display.update()
            sleep(interval)

#if __name__ == '__main__':
#    maze_file = 'mazes/dense/1a'
#    maze = np.genfromtxt(maze_file, dtype=str, delimiter=1).astype('bytes')
#    display = PacScreen(maze)
#    best = sa.sa_pacman(maze, wrong_path=True)
#    print(best)
#    display.run(best[0])
