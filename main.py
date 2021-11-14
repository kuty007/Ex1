import sys

from building import *
from elavator import *
import json
import math
from calls import *


def time_for_call(elv=Elevators, call=Callas):
    speed = float(elv.speed)
    open = float(elv.open_time)
    close = float(elv.close_time)
    start = float(elv.start_time)
    stop = float(elv.stop_time)
    src = int(call.src_floor)
    dst = int(call.dst_floor)
    time_to_complete = (abs(src - dst) / speed) + (2 * (open + close) + (start + stop))
    return time_to_complete


def unbusy_elv(building=Building, call=Callas):
    el = building.elvators
    elv_id = -1
    min_time = 9223372036854775807
    for t in range(len(el)):
        if len(el[t].time_busy) <= 0:
            temp = time_for_call(el[t], call)
            if temp < min_time:
                min_time = temp
                elv_id = t
    return elv_id


def add_time_busy(elv=Elevators, call=Callas):
    elv.time_busy.append(time_for_call(elv, call) + float((call.time)))


def delete_busy(bui=Building, call=Callas):
    for q in bui.elvators:
        if len(q.time_busy) > 0:
            for busy in q.time_busy:
                if busy < float(call.time):
                    q.time_busy.pop(q.time_busy.index(busy))


def allocate(build=Building, call=Callas):
    chosen_elv = -1
    min_time = 9223372036854775807
    delete_busy(build, call)
    free_elev = unbusy_elv(build, call)
    if free_elev != -1:
        call.elv_id = free_elev
        build.elvators[free_elev].calls_for_elv.append(call)
        add_time_busy(build.elvators[free_elev], call)
        return free_elev
    else:
        for r in range(len(build.elvators)):
            temp = abs(build.elvators[r].time_busy[-1] - float(call.time))
            if temp < min_time:
                min_time = temp
                chosen_elv = r
        call.elv_id = chosen_elv
        build.elvators[chosen_elv].calls_for_elv.append(call)
        add_time_busy(build.elvators[chosen_elv], call)
    return chosen_elv


x = load_csv_calls("Calls_b.csv")
b = Building(0, 8)
b.load_json_build("B4.json")
for i in x:
    allocate(b, i)
    print(i)
