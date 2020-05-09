import matplotlib.pyplot as plt
import pandas as pd 

a_p1 = pd.read_csv("data/astar/problem1/types_mean.csv") 
a_p2 = pd.read_csv("data/astar/problem2/types_mean.csv")

dfs_p1 = pd.read_csv("data/dfs/nomaze/types_mean.csv")
dfs_p2 = pd.read_csv("data/dfs/maze/types_mean.csv")

bfs_p1 = pd.read_csv("data/bfs/problem1/types_mean.csv")
bfs_p2 = pd.read_csv("data/bfs/problem2/types_mean.csv")

index = ['A*', 'BFS', 'DFS']
prob1 = [a_p1.loc[0,'time_100avg'], bfs_p1.loc[0,'time_1avg'], dfs_p1.loc[0,'time_1avg']] 
prob2 = [a_p2.loc[0,'time_100avg'], bfs_p2.loc[0,'time_1avg'], dfs_p2.loc[0,'time_1avg']]
dfp1 = pd.DataFrame(prob1, index=index)
dfp2 = pd.DataFrame(prob2, index=index)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot() # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.2

dfp1.plot(kind='bar', color='red', ax=ax, width=width, position=1)
dfp2.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)


colors = {'Problem 1':'red', 'Problem 2':'blue'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

ax.set_ylabel('Problem 1 (s)')
ax2.set_ylabel('Problem 2 (s)')

plt.show()