from building import Building
from elavator import Elevators
import json
import pandas as pd
p =Building(0,0,[])
p.load_json("B5.json")
x= p.max_floor
print(x)


train_data = pd.read_csv(r"Calls_a.csv")
print(train_data)