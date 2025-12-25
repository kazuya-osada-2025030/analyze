import os
import pandas as pd
print(f'現在の作業フォルダはここです：{os.getcwd()}')
test_data = {'col1':[1,2,3,4],'col2':[5,6,7,8]}
df_test = pd.DataFrame(test_data)
print(df_test)