from world import *
from individual import *
from group import *
import random
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import pdb

M = 10
n = 100
STEPS = 100
RUNS = 10
GRANULARITY = 50


initial_groups = []

for m in range(M):
    group = Group([])

    for k in range(n):
        new_level_of_coop = random.choice([1,0])
        new_individual = Individual(new_level_of_coop)
        group.add_member(new_individual)

    initial_groups.append(group)


fig, ax = plt.subplots()
x = np.linspace(0,0.05, num= GRANULARITY)

matrix_of_runs = []
for run in range(RUNS):
    run_series = []
    for i in range(GRANULARITY):
        migration = 0.05*i/50
        world = World(initial_groups, B = 10, eta = 0, mu = migration)
        for j in range(STEPS):
            world.make_transition()
        total_population = sum([group.size for group in world.groups])
        total_cooperators = sum([group.num_of_coops for group in world.groups])
        run_series.append(total_cooperators/total_population)
    matrix_of_runs.append(run_series)
    print(run)
#pdb.set_trace()
avg_of_runs = []
for i in range(GRANULARITY):
    across_runs = []
    for run in range(RUNS):
        across_runs.append(matrix_of_runs[run][i])
    avg_of_runs.append(mean(across_runs))

avg_of_runs_array = np.array(avg_of_runs)

ax.plot(x, avg_of_runs_array, label = 'eta = 0')



matrix_of_runs = []
for run in range(RUNS):
    run_series = []
    for i in range(GRANULARITY):
        migration = 0.05*i/50
        world = World(initial_groups, B = 10, eta = 0.006, mu = migration)
        for j in range(STEPS):
            world.make_transition()
        total_population = sum([group.size for group in world.groups])
        total_cooperators = sum([group.num_of_coops for group in world.groups])
        run_series.append(total_cooperators/total_population)
    matrix_of_runs.append(run_series)
    print(run)

avg_of_runs = []
for i in range(GRANULARITY):
    across_runs = []
    for run in range(RUNS):
        across_runs.append(matrix_of_runs[run][i])
    avg_of_runs.append(mean(across_runs))

avg_of_runs_array = np.array(avg_of_runs)

ax.plot(x, avg_of_runs_array, label = 'eta = 0.06', color = 'r')



ax.set_xlabel('migration')
ax.set_ylabel('average contribution level')
ax.legend()

plt.show()
