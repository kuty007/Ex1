import csv
import pandas as pd


class Callas:
    def __init__(self, time, src_floor, dst_floor, elv_id):
        self.time = time
        self.src_floor = src_floor
        self.dst_floor = dst_floor
        self.elv_id = elv_id

    def load_json_calls(self, file):
        

