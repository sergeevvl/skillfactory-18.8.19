age = list()
total = 0

try:
    tickets = int(input("Please enter the number of tickets you wish to purchase: "))
    for i in range(1, tickets + 1):
        age.append(input("Please enter visitor's age for the ticket No " + str(i) + ": "))
        if int(age[i-1]) < 18:
            print("This ticket will be free")
            total = total + 0
        elif 25 > int(age[i-1]) > 17:
            print("This ticket will cost you 990 RUB")
            total = total + 990
        elif int(age[i-1]) > 24:
            print("This ticket will cost you 1390 RUB")
            total = total + 1390
except ValueError as e:
    print("Please enter a correct value")
else:
    print("___")
    if tickets < 3:
        print("You wish to purchase ",str(tickets), " tickets and this'll cost you ", str(total), " RUB")
    elif tickets >= 3:
        print("You wish to purchase ",str(tickets), " tickets and with 10% discount this'll cost you ", str(total*0.9), " RUB")

