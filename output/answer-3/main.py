import pandas as pd
import numpy as np
ans = pd.read_csv('/input/question3/main.csv')
ans.Team.nunique()
ans.shape[1]
result = ans[['Team', 'Yellow Cards', 'Red Cards']]
result.sort_values(by=['Red Cards', 'Yellow Cards'], inplace = True)
result
