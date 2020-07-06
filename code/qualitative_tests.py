from world import *
from individual import *
from group import *
import random


# Test 1

n = 10
steps = 100

group_coops = Group([])
group_defs = Group([])

for i in range(n):
    coop_individual = Individual(1)
    group_coops.add_member(coop_individual)

    def_individual = Individual(0)
    group_defs.add_member(def_individual)

world = World([group_coops, group_defs], eta = 0, mu = 0, W = 2 )

for step in range(steps):
    world.make_transition()

size_1 = world.groups[0].size
size_2 = world.groups[1].size

print(f'The group of cooperators has {size_1} members, the one of defectors has {size_2}')


# Test 2

n = 10
steps = 100

group = Group([])
for i in range(n):
    coop_individual = Individual(1)
    group.add_member(coop_individual)

def_individual = Individual(0)
group.add_member(def_individual)

world = World([group], eta = 0, mu = 0)
for step in range(steps):
    world.make_transition()

coops = world.groups[0].num_of_coops
defs = world.groups[0].num_of_defs

print(f'There are {coops} cooperators and {defs} defectors')
