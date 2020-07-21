import random
from individual import *
class Group:

    def __init__(self, initial_population, id):
        self.population = initial_population
        self.size = 0
        self.contributions = 0
        #self.num_of_coops = 0
        #self.num_of_defs = 0
        self.id = id
        self.update()

    def update(self):
        self.size = len(self.population)
        coop_levels = [individual.coop_level for individual in self.population]
        self.contributions = sum(coop_levels)

    def add_member(self, individual):
        self.population.append(individual)
        self.update()
#
    # def kill_random_member(self):
        # random_position = random.randint(0,self.size-1)
        # del self.population[random_position]
        # self.update()
#
    # def kill_random_defector(self):
        # random_position = random.randint(0,self.size-1)
        # random_member = self.population[random_position]
        # while random_member.coop_level != 0:
            # random_position = random.randint(0,self.size-1)
            # random_member = self.population[random_position]
        # del self.population[random_position]
        # self.update()
#
    # def kill_random_cooperator(self):
        # random_position = random.randint(0,self.size-1)
        # random_member = self.population[random_position]
        # while random_member.coop_level != 1:
            # random_position = random.randint(0,self.size-1)
            # random_member = self.population[random_position]
        # del self.population[random_position]
        # self.update()
#
