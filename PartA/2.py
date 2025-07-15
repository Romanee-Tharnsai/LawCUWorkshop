Thaiyear = int(input("Enter Thai year:"))
year = Thaiyear-543
if year % 400 == 0:
    print("This number is a leap year")
elif year % 100 == 0:
    print("This number is not a leap year")
elif year % 4 == 0:
    print("This number is a leap year")
else:
    print("This number is not a leap year")