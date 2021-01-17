import pandas as pd
import numpy as np

df = pd.read_excel('test.xlsx')
col_category = ['CurrentEmployee', 'EligibleStudent', 'PermenentFacutly', 'Staff', 'Manager', 'Alumni']
col_all = []
col_active = []
col_active_percent = []

for d in col_category:
    all = df[(df[d]=='Yes')].count()[d]
    active = df[(df[d]=='Yes') & (df['IsActive']=='Yes')].count()[d]    
    active_percent =  "{0:.2%}".format((active / all) if all != 0 else 0)
    col_all.append(all)
    col_active.append(active)
    col_active_percent.append(active_percent)

d = {'category': col_category, 'All': col_all, 'Active': col_active, 'Active/All': col_active_percent}

df_result = pd.DataFrame(data=d)

print(df_result)

df_result.to_excel ('result.xlsx', index = False, header=True)