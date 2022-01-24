import pandas as pd
import numpy as np
users = pd.read_csv('https://github.com/Bungeetech/internship-test2/blob/master/input/question-2/main.csv', sep = '|')
print(users.groupby('occupation').age.min())
print(users.groupby('occupation').age.max())

