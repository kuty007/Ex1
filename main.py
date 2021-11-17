from building import *
from elavator import *
from calls import *


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


def add_time_busy(elv=Elevators, call=Callas, time_dif=None):
    elv.time_busy.append(time_for_call(elv, call) + float(call.time) + time_dif)


def delete_busy(bui=Building, call=Callas):
    for q in bui.elvators:
        if len(q.time_busy) > 0:
            for busy in q.time_busy:
                if busy < float(call.time):
                    q.time_busy.pop(q.time_busy.index(busy))


def busy_load(elv=Elevators):
    if len(elv.time_busy) == 5:
        return True


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
            temp = abs(build.elvators[r].time_busy[-1] - float(call.time))
            if temp < min_time:
                min_time = temp
                chosen_elv = r
        call.elv_id = chosen_elv
        build.elvators[chosen_elv].calls_for_elv.append(call)
        add_time_busy(build.elvators[chosen_elv], call, 0)
    return chosen_elv


def output(file_build, file_calls, file_update_calls):
    b = Building(0, 0)
    b.load_json_build(file_build)
    list_calls = load_csv_calls(file_calls)
    update_calls = []
    for i in list_calls:
        allocate(b, i)
        update_calls.append(i.__dict__.values())
    with open(file_update_calls, 'w', newline="") as f:
        csw = csv.writer(f)
        csw.writerows(update_calls)
    return file_update_calls


# def postion (elv = Elevators ,call):


output("B2.json", "Calls_b.csv", "output.csv")
