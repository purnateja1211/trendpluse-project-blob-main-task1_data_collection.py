import requests
import time
import json
import os
import csv
from datetime import datetime

catogories={
    "technology":["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews":	["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports":	["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science":["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment":	["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}
def stories_collection():
   story=[]
   if not os.path.exists("data"):
     os.makedirs("data")
   top_stories="https://hacker-news.firebaseio.com/v0/topstories.json"
   headers={"User-Agent":"TrendPulse/1.0"}
   result=requests.get(top_stories,headers=headers).json()
   ids=result[:500:] #get 500 stories 
#loop through each category
   for cat_name, keyword in catogories.items():
      print(f"~~~ Searching for {cat_name}~~~")
      found_in_cat=0

      for story_id in ids:
        if found_in_cat>=25: #stop if we get a 25 stories
            break

        try:
           item_data=requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", headers=headers).json()
         #print(item_data)
           if not item_data or "title" not in item_data:
              continue
           headline=item_data["title"].lower()
        # checking for  if any keyword matches with title
           if any(word.lower() in headline for word in keyword):
          #dict for task_1
            clean={
              "post_id": item_data.get("id"),
                        "title": item_data.get("title"),
                        "category": cat_name,
                        "score": item_data.get("score", 0),
                        "num_comments": item_data.get("descendants", 0),
                        "author": item_data.get("by"),
                        "collected_at": str(datetime.now())
          }
            story.append(clean)
            found_in_cat+=1
        except:
          continue
          #wait 2 sec between each catogry
      time.sleep(2)  
      today=datetime.now().strftime("%Y%m%d")  
      output_file=f"data/trends_{today}.json"
#finaly saving stories in file
   with open(output_file,"w") as f:
        json.dump(story,f,indent=4)
   print(f"Done! collected {len(story)} items into {output_file}")
if __name__ == "__main__":
    stories_collection()

