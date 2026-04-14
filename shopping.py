shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
#Task-1
shopping_list.append({"item": "Butter", "price": 80})
shopping_list.pop(0)
print(shopping_list)
#Task-2
total=0
for product in shopping_list:
    total+=product["price"]
    average=total/4
max_item=max(shopping_list,key=lambda items: items["price"])
print("Item:", max_item["item"])
print("Price:", max_item["price"])    
print(f"Total:{total}")    
#Task-3
summary={
  "total_items":4,
  "total_cost":290,
  "average_price":72.50
}
print(summary)