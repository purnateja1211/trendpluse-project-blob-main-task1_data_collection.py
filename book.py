tickets = int(input("Enter how many tickets (0-15): "))

ages = []
count = 1

while tickets > 0:
    age = int(input(f"Enter age of person {count}: "))
    ages.append(age)
    tickets -= 1
    count += 1

print("All ages:", ages)
