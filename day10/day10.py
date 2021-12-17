#%%
from math import floor

def open_file(filename):
    with open(filename) as f:
        return(f.readlines())

def solve(input_list):
    part1_score = 0
    part2_scores = []
    for line in input_list:
        tags = parse_line(line)
        if len(tags) == 1:
            part1_score += count_score_part1(tags)
        else:
            part2_scores.append(count_score_part2(tags))
    print_results(part1_score,part2_scores)

def parse_line(line):
    starting_tags = "([{<"
    result = ""
    for tag in line:
        if tag in starting_tags:
            result += tag
        else:
            if closing_tag_matches_last_open_tag(result,tag):
                result = remove_last_tag(result)
            else:
                return tag
    return result

def closing_tag_matches_last_open_tag(result,tag):
    tag_dicts = {")":"(","]":"[","}":"{",">":"<"}
    return result[-1] == tag_dicts[tag]

def remove_last_tag(result):
    return result[:-1]

def complete_line(line):
    tag_dicts = {"(":")","[":"]","{":"}","<":">"}
    result = ""
    for ch in line[::-1]:
        result += tag_dicts[ch]
    return result

def count_score_part1(tag):
    points_table = {")":3,"]":57,"}":1197,">":25137}
    return points_table[tag]

def count_score_part2(line):
    tags = complete_line(line)
    points_table = {")":1,"]":2,"}":3,">":4}
    score = 0
    for ch in tags:
        score *= 5
        score += points_table[ch]
    return score

def print_results(part1_score,part2_scores):
    print("Part 1:",part1_score)    
    print("Part 2:",sorted(part2_scores)[floor(len(part2_scores)/2)])

input_list = open_file("day10.txt")
input_list = [x.strip() for x in input_list]
solve(input_list)
# %%
