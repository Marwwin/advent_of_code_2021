# %%
from datetime import date, datetime

from typing import Counter


def solve(n):
    start = datetime.now()
    template, pairs = parse_input()
    result = generate_dict(template, pairs)
    for _ in range(n):
        result = step_one(result, pairs)
    count = count_elements(result, template)
    print(datetime.now() - start)

    print_result(count)


def parse_input():
    input_list = open_file("day14.txt")
    template = input_list[0].strip()
    pairs = {x.split(" -> ")[0]: x.strip().split(" -> ")[1]
             for x in input_list[2:]}
    return template, pairs


def open_file(filename: str) -> list[str]:
    with open(filename) as f:
        return(f.readlines())


def step_one(result, pairs):
    new_dic = {x: 0 for x in pairs.keys()}
    for key in result.keys():
        new_ch = pairs[key]
        one = key[0] + new_ch
        two = new_ch + key[1]
        if result[key] != 0:
            new_dic[one] += result[key]
            new_dic[two] += result[key]
    return new_dic


def count_elements(result, template):
    elements_in_result = {x: 0 for x in set("".join(result.keys()))}
    elements_in_result[template[0]] += 1
    elements_in_result[template[-1]] += 1
    for key in result.keys():
        one, two = key
        elements_in_result[one] += result[key]
        elements_in_result[two] += result[key]
    return {x: elements_in_result[x]/2 for x in elements_in_result.keys()}


def generate_dict(template, pairs):
    new_dict = {x: 0 for x in pairs.keys()}
    for i in range(len(template)-1):
        pair = template[i] + template[i+1]
        if pair not in new_dict.keys():
            new_dict[pair] = 1
        else:
            new_dict[pair] += 1
    return new_dict


def print_result(count):
    count = Counter(count)
    print(count.most_common()[0][1] - count.most_common()[-1][1])


solve(10)
solve(40)

# %%
