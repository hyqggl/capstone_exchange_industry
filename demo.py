import numpy as np
import pandas as pd
import matplotlib as plt


print("capstone project, hello world.")
test = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
test = test.cumsum()
# test.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=test.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()


