from world import *
from individual import *
from group import *
import random
import numpy as np
import matplotlib.pyplot as plt

M = 2
n = 100
TIME = 3


initial_groups = []

for m in range(M):
    group = Group([],m)

    for k in range(n):
        new_level_of_coop = random.choice([1,0])
        new_individual = Individual(new_level_of_coop)
        group.add_member(new_individual)

    initial_groups.append(group)

world = World(initial_groups, eta = 0.006, mu = 0.006, B = 100, W = 100)

avg_contr_series = []
group_population_series = []
time_series = []

time = 0
num_of_transitions = 0
while time < TIME:
    world.make_transition()
    time += world.waiting_times[num_of_transitions]
    num_of_transitions += 1
    print(time)

    avg_contribution = 0
    selected_group = world.groups[0]
    if selected_group.size != 0:
        avg_contribution = selected_group.num_of_coops/selected_group.size
    avg_contr_series.append(avg_contribution)
    group_population_series.append(selected_group.size)
    time_series.append(time)

avg_contr_series_array = np.array(avg_contr_series)
group_population_series_array = np.array(group_population_series)
time_series_array = np.array(time_series)

fig, ax1 = plt.subplots()
ax1.plot(time_series_array, avg_contr_series_array, label = 'Average contribution in group')

ax1.set_xlabel('time')
ax1.set_ylabel('Average level of cooperation')
ax1.set_title('Analogue of Figure 1')
#ax1.legend()

ax2 = ax1.twinx()
ax2.plot(time_series_array, group_population_series_array, label = 'Group size', color = 'r')
ax2.set_ylabel('group size')
ax2.legend()

plt.show()
