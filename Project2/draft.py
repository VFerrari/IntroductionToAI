# Since the fitness values are far to close to eachother, 
# the chosen selection methods to handle the mating was
# the rank selection as well as the tournament selection
# since these work well with idividual with near identical
# fitness values. These will also behave well in case we
# choose fitness functions which can have negative values.

from random import sample,randint,shuffle 
from numpy.random import choice # This name might be taken
from itertools import combinations as combine
import numpy as np

def match_couples(self, winners, P=2, T=float('inf')):
    # Combination: given a pool of winners, pairs then in couples
    #  - Each individual can mate with at most P other individuals
    #  - Each individual cannot mate twice with some individual
    #  - Each individual cannot mate with himself
    # This combination generates min(P*|winners|,T) pairs with the previous restrictions
    # Since each individual can generate at most P couples, there won't be more than P*|winners|
    # couples and, if T is smaller than  P*|winners|, there will be T couples.
    pairs = {x:set() for x in winners}
    couples = []

    print(winners)
    while len(winners) >= 2 and len(self.mates) <= T:
        invalid = []
        # Picks a father and remove any mate which he was already paired with
        dad = winners.pop(np.random.randint(len(winners)))
        for i,w in enumerate(winners):
            if w in pairs[dad]: invalid.append(winners.pop(i))

        # Picks a mother and returns the removed pairs to the winners pool
        mom = winners.pop(np.random.randint(len(winners)))
        
        # Update mating registry and return invalid matches to winners pool
        pairs[dad].add(mom)
        pairs[mom].add(dad)
        winners += invalid
        
        # Update the couples for reproduction
        couples.append((dad,mom))
        
        # Only allows the selected couple to participate again if they haven't
        # mated with 2 or more individuals.
        if len(pairs[dad]) < P: winners.append(dad)
        if len(pairs[mom]) < P: winners.append(mom)
        shuffle(winners)

    return couples

# if the tournament size is larger, weak individuals have 
# a smaller chance to be selected, because, if a weak 
# individual is selected to be in a tournament, there is 
# a higher probability that a stronger individual is also 
# in that tournament.

def tournament(self, k, N, P, T):
    pool = list(range(self.pop_size))
    pairs = {x:set() for x in pool}
    fitness = lambda x: self.all_fits[x]
    winners,self.mates = [],[]

    # Run tournament to pick N winners
    while len(winners) < N:
        competitors = np.random.choice(pool, size=k, replace=False)
        winner = max(competitors, key=fitness)
        winners.append(winner)
        pool.remove(winner) # remove winner from pool
    
    for (dad,mom) in combine(winners, 2):
        if (len(pairs[dad]) < P) and (len(pairs[mom]) < P): 
            pairs[dad].add(mom)
            pairs[mom].add(dad)
            self.mates.append((dad,mom))
            if len(self.mates) == T: break
        
class Test:
    def __init__(self):
        self.population = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.pop_size = len(self.population)
        self.all_fits = [randint(0,11) for i in range(self.pop_size)]
        self.mates = None

test = Test()
# tournament(test, 4, 2)
# print(test.mates)