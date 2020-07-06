import random
from group import *
from individual import *
import pdb

class World:

    def __init__(self, initial_groups, W = 1, B = 1, R = 1, C = 1, eta = 0.01, mu = 0.01):
        self.groups = initial_groups
        self.waiting_times = []

        self.W = W
        self.B = B
        self.R = R
        self.C = C
        self.eta = eta
        self.mu = mu

    def payoff_coops(self, group):
        payoff = 0
        if group.size != 0:
            payoff = min(1,self.B / group.size)  * group.num_of_coops    # This depends on the model
        return payoff

    def payoff_defs(self, group):
        payoff = 0
        if group.size != 0:
            payoff = 1 + min(1,self.B / group.size)  * group.num_of_coops  # This depends on the model
        return payoff

    def birth_rate_coops(self, group):
        rate = self.C * self.payoff_coops(group)  # This depends on the model
        return rate

    def birth_rate_defs(self, group):
        rate  = self.C * self.payoff_defs(group)   # This depends on the model
        return rate

    def second_level_rate(self, group):
        rate = 0
        list_of_non_empty_groups = []
        for internal_group in self.groups:
            if internal_group.size > 0:
                list_of_non_empty_groups.append(1)
        num_of_non_empty_groups = sum(list_of_non_empty_groups)
        condition = (group.size != 0) and (num_of_non_empty_groups > 1)
        if condition:
            rate = self.W * ( 1 + self.R * group.num_of_coops / group.size)    # This depends on the model
        return rate

    def create_new_individual(self, group, level_of_coop):
        group.kill_random_member()

        there_is_mutation = random.choices([1,0], [self.eta, 1-self.eta])[0]
        if there_is_mutation:
            level_of_coop = 1-level_of_coop

        new_individual = Individual(level_of_coop)

        there_is_migration = random.choices([1,0], [self.mu, 1-self.mu])[0]
        if there_is_migration:
            new_group = random.choice(self.groups)
            while new_group == group:
                new_group = random.choice(self.groups)
            new_group.add_member(new_individual)
        else:
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

        #pdb.set_trace()

        list_of_rates = [self.birth_rate_coops(group) * group.num_of_coops  + self.birth_rate_defs(group) * group.num_of_defs + self.second_level_rate(group) for group in self.groups]

        global_rate = sum(list_of_rates)

        #pdb.set_trace()

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
