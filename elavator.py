from calls import Callas
import math


class Elevators:
    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time,
                 calls_for_elv, time_busy):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.calls_for_elv = calls_for_elv
        self.time_busy = time_busy

    def __repr__(self) -> str:
        return f"repr _id:{self.id} speed:{self.speed} min_floor:{self.min_floor} " \
               f"max_floor:{self.max_floor} close_time:{self.close_time} " \
               f"open_time:{self.open_time} start_time:{self.stop_time} stop_time:{self.stop_time} calls_for_elv:{self.calls_for_elv}" \
               f"time_busy:{self.time_busy} "
