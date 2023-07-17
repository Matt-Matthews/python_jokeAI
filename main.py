import pandas as pd

data_file_path = "./data/melb_data.csv"

model_data = pd.read_csv(data_file_path)

model_data.describe()

print(model_data)




# from learntools.core import binder
# binder.bind(globals())
# from learntools.machine_learning.ex2 import *
# print("Setup Complete")