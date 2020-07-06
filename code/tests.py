from world import *
from individual import *
from group import *
import random
import pdb


# Test 1
single_individual = Individual(1)
initial_group = Group([single_individual])
world = World([initial_group], eta = 0, mu = 0)
flag = True
i = 0
while flag and i < 100:
    world.make_transition()
    group = world.groups[0]
    population = group.size
    if population != 1:
        flag = False
        print('test 1 failed')
    i += 1

if flag:
    print('test 1 passed')


# Test 2
single_individual = Individual(1)
initial_group_1 = Group([single_individual])
initial_group_2 = Group([])
world = World([initial_group_1, initial_group_2], eta = 0, mu = 1)
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

if flag:
    print('test 2 passed')



# Test 3
single_individual =  Individual(1)
initial_group = Group([single_individual])
world = World([initial_group], eta = 1, mu = 0)
flag = True
i = 0
while flag and i < 100 :
     world.make_transition()
     individual = world.groups[0].population[0]
     if (i%2 == 0 and individual.coop_level == 1) or (i%1 == 1 and individual.coop_level == 0):
         flag = False
         print('test 3 failed')
     i+=1

if flag:
    print('test 3 passed')
