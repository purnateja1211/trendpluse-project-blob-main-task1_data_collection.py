import pandas as pd
import numpy as np
df=pd.read_csv("trends_clean.csv")
print(f"load: {df.shape}") 
print(" the first 5 rows is :")
print(df.head())
print(f' shape of data frame is :{df.shape}')
print( f" Average score is :{df['score'].mean()}")
print(f" Average comments is  :{df['num_comments'].mean()}")
print("------numpy stats------")
print(f"mean score:{df['score'].mean()}")
print(f'meadian score :{df["score"].median()}')
print(f"standard deviation is : {df['score'].std()}")
print(f" aximum score :{df['score'].max()}")

print(f"minimum score :{df['score'].min()}")

print(f"most stories is in :{df['category'].value_counts().index[0]} ({df['category'].value_counts().max()}) ")
maxcomments=df['num_comments'].max()
most_commented_story=df[df['num_comments']==maxcomments]
print(f"Most commented  story is :{most_commented_story['title'].iloc[0]}- {maxcomments} comments")
df['engagement']=df['num_comments']/df['score']+1
avg=df['score'].mean()

df['is_popular']=df['score']>avg

df.to_csv("data/trends_analysed.csv",index=False)
print("saved to trends_analysed.csv")
