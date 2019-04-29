#EDA
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/yuyoungsu/Documents/LAB/2. Business Intelligence/3. 6차년도/4. ODA_SNA_v2/DB_WB_Vietnam_ODA_SNUT_190327.csv',header=0)

len(data['Notice_No'].value_counts()) #103
len(data['Name'].value_counts())


#Team일 때, 단독일 때 낙찰성공률
team = data.loc[(data.JV=='Leader')]