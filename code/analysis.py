from world import *
from individual import *
from group import *
import random

M = 3
n = 10
STEPS = 100


initial_groups = []

for m in range(M):
    group = Group([])

    for k in range(n):
        new_level_of_coop = random.choice([1,0])
        new_individual = Individual(new_level_of_coop)
        group.add_member(new_individual)

    initial_groups.append(group)

world = World(initial_groups)

for step in range(STEPS):
    world.make_transition()
    print(world.waiting_times[step])
