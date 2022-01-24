import numpy as np
import pandas as pd
result = pd.read_csv('/input/question1/main.csv')
result.head()
result.set_index('Year', drop=True, inplace=True)
result.head()
result.drop(columns='Total', inplace=True)
result.head()
results = result.resample('10AS').sum()
results['Population'] = result['Population'].resample('10AS').max()
results
