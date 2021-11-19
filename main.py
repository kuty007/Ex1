from building import *
from elavator import *
from calls import *

"""
time_for_call
this function calculate the time that will take to complete Elevator call
"""


def time_for_call(elv=Elevators, call=Callas):
    if len(elv.calls_for_elv) < 1:
        dis_from_call = abs(0 - call.src_floor)
    else:
        dis_from_call = abs(elv.calls_for_elv[-1].dst_floor - call.src_floor)
    speed = float(elv.speed)
    open = float(elv.open_time)
    close = float(elv.close_time)
    start = float(elv.start_time)
    stop = float(elv.stop_time)
    src = int(call.src_floor)
    dst = int(call.dst_floor)
    time_to_complete = ((abs(src - dst)) + dis_from_call) / speed + (2 * (open + close) + (start + stop))
    return time_to_complete


"""
unbusy_elv
this function  check if there is free elevators  in if so send the free elevator that will
complete the new call the fastest
"""


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


"""
add_time_busy
this function add the new time till this elevator will be finish the new call  
"""


def add_time_busy(elv=Elevators, call=Callas, time_dif=None):
    elv.time_busy.append(time_for_call(elv, call) + float(call.time) + time_dif)


"""
delete_busy
this function delete all the times of calls that were already complete by this time
to make sure that we will know when the elevator is free 
"""


def delete_busy(bui=Building, call=Callas):
    for q in bui.elvators:
        if len(q.time_busy) > 0:
            for busy in q.time_busy:
                if busy < float(call.time):
                    q.time_busy.pop(q.time_busy.index(busy))


"""
allocate
this function allocate an elevator for a call by first check if there is a free elevator to send
and if not check which elevator is the closest to finish her calls ans send her
"""


def allocate(build=Building, call=Callas):
    chosen_elv = -1
    min_time = 9223372036854775807
    delete_busy(build, call)
    free_elev = unbusy_elv(build, call)
    if free_elev != -1:
        call.elv_id = free_elev
        build.elvators[free_elev].calls_for_elv.append(call)
        add_time_busy(build.elvators[free_elev], call, 0)
        return free_elev
    else:
        for r in range(len(build.elvators)):
            temp = abs(build.elvators[r].time_busy[-1] - float(call.time) + time_for_call(build.elvators[r], call))
            if temp < min_time:
                min_time = temp
                chosen_elv = r
        call.elv_id = chosen_elv
        build.elvators[chosen_elv].calls_for_elv.append(call)
        add_time_busy(build.elvators[chosen_elv], call, min_time)
        build.elvators[chosen_elv].time_busy = sorted(build.elvators[chosen_elv].time_busy)
    return chosen_elv
