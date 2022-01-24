import pandas as pd
import numpy as np
users = pd.read_csv('/input/question3/main.csv', sep = '|')
print(users.groupby('occupation').age.min())
print(users.groupby('occupation').age.max())

