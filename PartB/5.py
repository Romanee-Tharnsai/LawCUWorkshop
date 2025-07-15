days=["day 1","day 2","day 3","day 4","day 5","day 6","day 7"]
amounts = []
for i in range(7):
    amount = input("Enter amount of money you used on day " + str(i+1) + "?")
    amounts.append(amount)
average = sum(amounts) / 7
maximum = max(amounts)

print("Average amount of money used per day:"+ str(average))
print("Maximum amount of money used per day:" + str(maximum))