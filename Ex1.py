from building import *
from elavator import *
from calls import *
import sys
from main import *


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


inp = sys.argv
if len(inp) > 3:
    b_path, i_path, o_path = inp[1], inp[2], inp[3]
output(b_path, i_path, o_path)

output("B3.json", "Calls_a.csv", "output.csv")