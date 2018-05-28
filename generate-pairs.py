#!/usr/bin/env python3

import random
from collections import deque
from copy import copy
from weekly_input import *
from gender_db import *


def remove_devil_when_odd(babies):
    if len(babies) % 2:
        babies.remove(bigdevil)


def pick_one(baby, to_pick, picked, avails, opposit):
    a_gender = b_gender = gender_db[baby]
    if opposit:
        b_gender = a_gender ^ True
    candidates = deque(avails[int(b_gender)])
    while picked:
        baby_friend = candidates.popleft()
        if baby_friend not in picked:
            candidates.append(baby_friend)
        else:
            picked.remove(baby_friend)
            avails[int(b_gender)].remove(baby_friend)
            return baby_friend
    return ""


def init(babies):
    global gender_db
    random.seed(random_seed)
    female = list(filter(lambda x: gender_db[x], babies))
    male = list(filter(lambda x: not gender_db[x], babies))
    to_pick = deque(copy(babies[:len(babies) // 2]))
    picked = copy(babies[len(babies) // 2:])
    f_pick_m = min(len(set(female) & set(to_pick)),
                   len(set(male) & set(picked)))
    m_pick_f = min(len(set(female) & set(picked)),
                   len(set(male) & set(to_pick)))
    random.shuffle(female)
    random.shuffle(male)
    return [male, female], to_pick, picked, [m_pick_f, f_pick_m]


def main():
    global babies_sorted, gender_db, random_seed
    match_result = []
    babies = copy(babies_sorted)
    remove_devil_when_odd(babies)
    avails, to_pick, picked, pick_opposit_cnt = init(babies)
    while to_pick:
        baby = to_pick.popleft()
        oppo = bool(pick_opposit_cnt[int(gender_db[baby])])
        baby_friend = pick_one(baby, to_pick, picked, avails, oppo)
        match_result.append((baby, baby_friend))
        if oppo:
            pick_opposit_cnt[int(gender_db[baby])] -= 1

    for pair in match_result:
        print(pair[0], ":", pair[1])


if __name__ == '__main__':
    main()
