import pandas as pd
df=pd.read_json('Kickstarter_Kickstarter.json','r')
results=df["projects"]
with open('output.json','w') as file:
    pd.to_json(file)
