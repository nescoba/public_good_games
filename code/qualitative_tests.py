from world import *
from individual import *
from group import *
import random


# Test 1

n = 10
steps = 100

group_coops = Group([],1)
group_defs = Group([],0)

for i in range(n):
    coop_individual = Individual(1)
    group_coops.add_member(coop_individual)

    def_individual = Individual(0)
    group_defs.add_member(def_individual)

world = World([group_coops, group_defs], eta = 0, mu = 0 )

for step in range(steps):
    world.make_transition()

group_coops = world.groups[0]
group_defs = world.groups[1]
if group_coops.id != 1:
    group_coops = world.groups[1]
    group_defs = world.groups[0]

size_coops = group_coops.size
size_defs = group_defs.size

print(f'The group of cooperators has {size_coops} members, the one of defectors has {size_defs}')


# Test 2

n = 10
steps = 100

group = Group([],0)
for i in range(n):
    coop_individual = Individual(1)
    group.add_member(coop_individual)

for i in range(n//3):
    selfish_individual = Individual(0)
    group.add_member(selfish_individual)

world = World([group], eta = 0, mu = 0)
for step in range(steps):
    world.make_transition()

coops = world.groups[0].num_of_coops
defs = world.groups[0].num_of_defs

print(f'There are {coops} cooperators and {defs} defectors')
