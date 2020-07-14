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

world = World([group_coops, group_defs], eta = 0, mu = 0, W = 2 )

for step in range(steps):
    world.make_transition()

size_1 = world.groups[0].size
size_2 = world.groups[1].size

print(f'The group of cooperators has {size_1} members, the one of defectors has {size_2}')


# Test 2

n = 10
steps = 100

group = Group([],0)
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


# Test 3
single_individual = Individual(1)
initial_group_1 = Group([single_individual], 0)
initial_group_2 = Group([], 1)
world = World([initial_group_1, initial_group_2], eta = 0, mu = 1000000)
flag = True
i = 0
while flag and i < 100:
    #pdb.set_trace()
    world.make_transition()
    size_1 = world.groups[0].size
    size_2 = world.groups[1].size
    if (i%2 == 0 and size_1 != 0) or (i%2 == 1 and size_2 != 0):
        flag = False
        print('test 2 failed')
    i += 1
#
if flag:
    print('test 2 passed')
