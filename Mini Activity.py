
print("How old are you?")
age = input()
try: 
    age = int(age)
except ValueError:
    age = input("Please enter a valid age: ")
married = input("Are you married? 'Yes'or'No'")