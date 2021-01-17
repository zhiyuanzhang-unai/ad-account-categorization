import pandas as pd
import numpy as np

df = pd.read_excel('test.xlsx')
col1 = ['IsActive', 'Passwordchange', 'CurrentEmployee', 'EligibleStudent', 'PermenentFacutly', 'Staff', 'Manager', 'Alumni']
col2 = []

for d in col1:
    data = df[df[d]=='Yes'].count()[d]
    col2.append(data)

d = {'category': col1, 'count': col2}

df_result = pd.DataFrame(data=d)

df_result.to_excel ('result.xlsx', index = False, header=True)