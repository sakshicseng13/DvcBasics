import pandas as pd

data=[
    
    {"name":"sakshi","age":30,"city":"bhopal"},
    {"name":"priyesh","age":35,"city":"Jajpur"},
    {"name":"Ishita","age":29,"city":"delhi"},
    {"name":"Jaya","age":36,"city":"Shahdol"}
]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)