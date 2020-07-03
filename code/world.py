import random
from group import *
from individual import *

class World:

    def __init__(self, initial_groups):
        self.groups = initial_groups
        self.waiting_times = []

        self.W = 1
        self.B = 1
        self.R = 1
        self.C = 1

    def payoff_coops(self, group):
        payoff =  self.B * group.num_of_coops / group.size   # This depends on the model
        return payoff

    def payoff_defs(self, group):
        payoff = 1 + self.B * group.num_of_coops / group.size  # This depends on the model
        return payoff

    def birth_rate_coops(self, group):
        rate = self.C * self.payoff_coops(group)  # This depends on the model
        return rate

    def birth_rate_defs(self, group):
        rate  = self.C * self.payoff_defs(group)   # This depends on the model
        return rate

    def second_level_rate(self, group):
        rate = self.W * ( 1 + self.R * group.num_of_coops / group.size)    # This depends on the model
        return rate

    def create_new_individual(self, group, level_of_coop):
        group.kill_random_member()
        new_individual = Individual(level_of_coop)
        group.add_member(new_individual)

    def execute_group_level_dynamic(self, chosen_group):
        copy_of_groups = self.groups.copy()
        copy_of_groups.remove(chosen_group)
        list_of_sizes = [group.size for group in copy_of_groups]
        second_chosen_group = random.choices(copy_of_groups, list_of_sizes)[0]
        second_chosen_group.kill_random_member()

        chosen_level_of_coop = random.choices([1,0], [chosen_group.num_of_coops , chosen_group.num_of_defs ])[0]
        new_individual = Individual(chosen_level_of_coop)
        chosen_group.add_member(new_individual)

    def make_transition(self):
        list_of_rates = [self.birth_rate_coops(group) * group.num_of_coops  + self.birth_rate_defs(group) * group.num_of_defs + self.second_level_rate(group) for group in self.groups]

        global_rate = sum(list_of_rates)

        waiting_time_until_new_event = random.expovariate(global_rate)
        self.waiting_times.append(waiting_time_until_new_event)

        chosen_group = random.choices(self.groups, list_of_rates)[0]



        group_list_of_rates = [self.birth_rate_coops(chosen_group) * chosen_group.num_of_coops, self.birth_rate_defs(chosen_group) * chosen_group.num_of_defs, self.second_level_rate(chosen_group)]

        chosen_event = random.choices(['coop', 'def', 'second_level'], group_list_of_rates)[0]

        if chosen_event == 'coop':
            self.create_new_individual(chosen_group, 1)
        elif chosen_event == 'def':
            self.create_new_individual(chosen_group, 0)
        else:
            self.execute_group_level_dynamic(chosen_group)
