tickets=int(input("enter how many tickets from 0 to 15: "))\
ages = []
count=1
while tickets > 0:
    ages=input(f"Enter age of each person {count}:")
    ages.append(age)
    count-=1
    tickets-=1
    
print(ages)    
