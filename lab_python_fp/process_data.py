import json
import os
from .field import field
from .gen_random import gen_random
from .unique import Unique
from .print_result import print_result
from .cm_timer import cm_timer_1

data_file = 'data_light.json'

@print_result
def f1(data):
    return sorted(set(Unique(field(data, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(data):
    return list(filter(lambda x: x.lower().startswith("программист"), data))

@print_result
def f3(data):
    return list(map(lambda x: f"{x} с опытом Python", data))

@print_result
def f4(data):
    salaries = list(gen_random(len(data), 100_000, 200_000))
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(data, salaries)]

if __name__ == '__main__':
    with open(data_file, encoding='utf-8') as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))
