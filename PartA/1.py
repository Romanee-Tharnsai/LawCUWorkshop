name = input("Enter last name: ")
if len(name) <= 15:
    print(name + 'SAT-compatible')
else:
    print("Not compatible")