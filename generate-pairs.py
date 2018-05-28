#!/usr/bin/env python
#
from copy import copy
from weekly_input import *
from baby_db import *


def remove_devil_when_odd(babies):
    if len(babies)%2:
        babies.remove(bigdevil)

def pick_one(baby, be_picked, avail):
    baby_gender = baby_db[baby]
    partner_gender = baby_gender ^ True
    candidates = avail[int(partner_gender)] if avail[int(partner_gender)] else avail[int(not partner_gender)]
    candidates = deque(candidates)
    while be_picked:
        baby_friend = candidates.popleft()
        if baby_friend not in be_picked:
            candidates.append(baby_friend)
        else:
            be_picked.remove(baby_friend)
            return baby_friend
    return ""

def init(babies):
    global baby_db
    female = randome.shuffle(filter(lambda x: baby_db[x], babies))
    male = randome.shuffle(filter(lambda x: not baby_db[x], babies))
    return [male, female]

def main():
    global babies_sorted
    match_result = []
    babies = copy(babies_sorted)
    remove_devil_when_odd(babies)
    available_list = init(babies)
    to_pick = deque(copy(babies[:len(babies)/2+1]))
    be_picked = copy(babies[len(babies)/2+1:])
    while to_pick:
        baby = to_pick.popleft()
        baby_friend = pick_one(baby, be_picked)
        match_result.append((baby, baby_friend))
    for pair in match_result:
        print (pair)

    
