import pandas as pd
rd=pd.read_json("sample_Data.json")

print('display 5 rows of first')
print(rd.head())

print('display 5 rows of last')
print(rd.tail())
