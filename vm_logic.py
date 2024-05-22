
# list of drinks and price
drinks = {
    '1': {'drink': '🟢 Matcha Latte ', 'price': 15.00},
    '2': {'drink': '🍊 Orange Juice', 'price': 10.00},
    '3': {'drink': '🍎 Apple Juice', 'price': 10.00},
    '4': {'drink': '🍇 Blackcurrent', 'price': 10.00},
    '5': {'drink': '🟢🍓 Strawberry Matcha Latte', 'price': 20.00},
    '6': {'drink': '🍉 Watermelon Latte', 'price': 20.00},
    '7': {'drink': '🍌 Banana Milk', 'price': 12.00},
    '8': {'drink': '💧Mineral Water', 'price': 2.00}
}


print("Axrail.ai Drinks")
print("Please select a drink:🍵")

# print out menu available
for k, i in drinks.items():
    print(f"{k}. {i['drink']} - RM{i['price']}")

# get input
choose = input("Enter the item id number to purchase:")

# number of notes to return
def calculate_notes(balance):
    denominations = [100, 50, 20,10,5,1]
    note_counts = {100:0, 50:0, 20:0, 10:0, 5:0,1:0}

    for d in denominations:
        note_counts[d], balance = divmod(balance, d)

    return note_counts

if choose in drinks:
    selected_item = drinks[choose]
    print(f"You have selected {selected_item['drink']}.")
    total_price = selected_item['price']

    while total_price > 0:
        try:
            payment = input(f"Please insert RM{total_price:.2f} (whole number only): ")
            if not payment.isdigit():
                raise ValueError("Invalid amount. Please enter a whole number.")
            payment = int(payment)
            if payment >= total_price:
                change = payment - total_price
                print(f"Thank you! Your change is RM {change:.2f}.")

                note_counts = calculate_notes(change)
                for denom, count in note_counts.items():
                    if count > 0:
                        print(f"RM {denom}: {count}")

                break
            else:
                print("Insufficient. Kindly provide the correct amount.")
                total_price -= payment
        except ValueError as e:
            print(e)
else:
    print("Invalid. Please try again.")
