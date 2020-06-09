'''
Assignment: Genetic Algorithm for the N-Queens problem.

Subject:
    MC906 - Introduction to Artificial Intelligence
Authors:
    Victor Ferreira Ferrari  - RA 187890

University of Campinas - UNICAMP - 2020

Last Modified: 09/06/2020.
'''

import numpy as np

N = 8
POP_SIZE = 4
MUT_RATE = 0.5
MAX_ITER = 15000

def nqueens_genetic():
    pop = gen_initial_population(POP_SIZE)
    
    # Fitness
    fit = []
    for i in pop:
        fit.append(fitness(i))
    fit = np.array(fit)
    
    # Best
    best_idx = np.argmax(fit)
    best_sol = pop[best_idx]
    best_val = fit[best_idx]
    
    # Stop criteria
    sol_val = np.arange(N).sum()
    iterations = 0
    
    while best_val < sol_val and iterations < MAX_ITER:
        
        # Roulette selection
        sel = selection(pop, fit, POP_SIZE)
    
        # Reproduction
        for i in range(0, len(sel), 2):
            pop[i], pop[i+1] = reproduction(sel[i], sel[i+1])
    
        # Mutation
        mutate_pop(pop, MUT_RATE)
        
        # Fitness
        for i in range(POP_SIZE):
            fit[i] = fitness(pop[i])
                
        # Update Max
        best_idx = np.argmax(fit)
        if fit[best_idx] > best_val:
            best_sol = pop[best_idx]
            best_val = fit[best_idx]
        
        iterations += 1
    
    # Board
    board = create_board(best_sol)
    print(board)
    
    print('Solution: ', best_sol)
    print('Iterations: ', iterations)
    print('Solution Value: ', best_val)
    

def gen_initial_population(amount):
    pop = []
    
    # Creating random states.
    for i in range(amount):
        code = np.random.randint(0, high=N, size=N)
        pop.append(code)
    
    return pop

def fitness(state):
        
    # Max value is the sum of elements in the range 0-N.
    value = np.arange(N).sum()
    
    # Check line.
    for j in range(len(state)):
        for i in state[j+1:]:
            value -= 1 if state[j]==i else 0
    
    # Check diagonals
    for j in range(len(state)):
        for i in range(j+1,len(state)):
            dx = state[i] - state[j]
            dy = i - j
            value -= 1 if dx == dy or dx == -dy else 0
    
    return value

def create_board(state):
    board = np.zeros((N,N))
    
    for i in range(len(state)):
        board[state[i],i] = 1
    
    return board

def selection(pop, fit, amount):
    
    # Roulette selection
    sel_idxs = np.random.choice(np.arange(amount), (amount), replace=True, p=fit/fit.sum())
    
    selected = []
    for idx in sel_idxs:
        selected.append(pop[idx])
    
    return selected    

def reproduction(x, y):
    # Single-point crossover: generate point
    point = np.random.randint(0, x.size-1)
    
    # Getting children
    c1 = np.concatenate([x[:point], y[point:]])
    c2 = np.concatenate([y[:point], x[point:]])
    
    return c1,c2

def mutate_pop(pop, rate):
    
    # Select states to mutate.
    mut_amount = int(rate*len(pop))
    mut_idx = np.random.randint(0, len(pop), mut_amount) 
    size = pop[0].size
    
    # Change element to random.
    for i in mut_idx:
        change = np.random.randint(0, size, 2)
        pop[i][change[0]] = change[1]
    

if __name__ == "__main__":
    nqueens_genetic()
