Pizza = 120
Pasta = 100
Cake = 120
Coffee = 150
GST = 1.0347  # GST as a multiplier (3.47% = 1.0347)

print("Welcome to Joe Cafe")
user_choice = input(f"Please select from the menu: Pizza ({Pizza}), Pasta ({Pasta}), Cake ({Cake}), Coffee ({Coffee}): ").strip().lower()

if user_choice == "pizza":
    amount_to_paid = Pizza * GST
    print(f"Your total amount is {amount_to_paid:.2f}")
elif user_choice == "pasta":
    amount_to_paid = Pasta * GST
    print(f"Your total amount is {amount_to_paid:.2f}")
elif user_choice == "cake":
    amount_to_paid = Cake * GST
    print(f"Your total amount is {amount_to_paid:.2f}")
elif user_choice == "coffee":
    amount_to_paid = Coffee * GST
    print(f"Your total amount is {amount_to_paid:.2f}")    
else:
    print("I am sorry, we don't have that on our menu. Would you like to order something else?")
