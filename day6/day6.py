#%%
import sys
sys.path.append('../lib')

import advent_of_code


class LanternFish:
    def __init__(self,inp) -> None:
        self.fishes = self.parse_input(inp)
        print(self.fishes)
    def parse_input(self,inp):
        fishes = {x:0 for x in range(9)}
        for i in inp[0].split(","):
            fishes[int(i)] += 1
        return fishes

    def age_days(self,n):

        for i in range(n):
            self.fishes = self.one_day()

    def one_day(self):
        fishes = {x:0 for x in range(9)}
        for f in list(reversed(self.fishes.keys())):
            if f == 0:
                fishes[8] = self.fishes[f]
                fishes[6] += self.fishes[f]
            else:
                fishes[f-1] = self.fishes[f]
        return fishes

    def print_result(self):
        print(sum(self.fishes.values()))

input_list = advent_of_code.open_file("day6.txt")
fish = LanternFish(input_list)
fish.age_days(80)
fish.print_result()
fish = LanternFish(input_list)
fish.age_days(256)
fish.print_result()
# %%
