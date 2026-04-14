import matplotlib.pyplot as plt
import pandas as pd
import os
df=pd.read_csv("trends_analysed.csv")
os.makedirs("outputs",exist_ok=True)#creatng file
top10=df.sort_values(by='score', ascending=False).head(10)
top10['title']=top10['title'].str[0:50]#shorten title for better visualization
plt.figure(figsize=(15,6))

plt.barh( top10['title'],top10['score'])
plt.xlabel("Scores")

plt.ylabel("Title")

plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()#invert y axis to show highest score at top
plt.savefig("outputs/chart1_top_stories.png")
plt.show()
df1=df['category'].value_counts()
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.figure(figsize=(10,6))

plt.bar(df1.index,df1.values, color=colors)
plt.xlabel("Categories")
plt.ylabel("Count_")

plt.title("Distribution of Stories by Category")
plt.xticks(rotation=45)

plt.savefig("outputs/chart2_categories.png")
plt.show()

colors =df["is_popular"].map({True: 'red', False: 'blue'})

plt.scatter(df['score'],df['num_comments'], color=colors)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Number of Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.show()