import random
from group import *
from individual import *
class World:

    def __init__(self initial_groups, comp_rate):
        self.groups = initial_groups
        self.comp_rate = comp_rate
        self.waiting_times = []

    def payoff_coops(group):
        payoff = group.num_of_coops / group.size   # TODO:implement specific function
        return payoff

    def payoff_defs(group):
        payoff = 1 + group.num_of_coops / group.size  # TODO:implement specific function
        return payoff

    def birth_rate_coops(self, group):
        return payoff_coops(group)

    def birth_rate_defs(self, group):
        return payoff_defs(group)

    def second_level_rate(self, group):
        rate = self.comp_rate * ( 1 + group.num_of_coops / group.size)    # TODO:implement specific function
        return rate

    def select_event(self):
        list_of_rates = [birth_rate_coops(group) * group.num_of_coops  + birth_rate_defs(group) * group.num_of_defs + second_level_rate(group) for group in self.groups]

        global_rate = sum(list_of_rates)

        waiting_time_until_new_event = random.expovariate(global_rate)
        self.waiting_times.append(waiting_time_until_new_event)

        chosen_group = random.choices(self.groups, list_of_probs)[0]



        group_list_of_rates = [birth_rate_coops(chosen_group) * chosen_group.num_of_coops, birth_rate_defs(chosen_group) * chosen_group.num_of_defs, second_level_rate(group)]

        chosen_event = random.choices(['coop', 'def', 'second_level'], group_list_of_rates)[0]

        if chosen_event == 'coop':
            new_individual = Individual(1)
            chosen_group.kill_random_member()
            chosen_group.add_member(new_individual)
        elif chosen_event == 'def':
            new_individual = Individual(0)
            chosen_group.kill_random_member()
            chosen_group.add_member(new_individual)
        else
            copy_of_groups = self.groups.copy()
            copy_of_groups.remove(chosen_group)
            list_of_sizes = [group.size for group in copy_of_groups]
            second_chosen_group = random.choices(copy_of_groups, list_of_sizes)[0]
            second_chosen_group.kill_random_member()

            chosen_level_of_coop = random.choices([1,0], [chosen_group.num_of_coops , chosen_group.num_of_defs ])[0]
            new_individual = Individual(chosen_level_of_coop)
            chosen_group.add_member(new_individual)
