import pandas as pd
import numpy as np
ans = pd.read_csv('/input/question3/main.csv')
result = ans[['Team', 'Yellow Cards', 'Red Cards']]
result.sort_values(by=['Red Cards', 'Yellow Cards'], inplace = True)
result
