''' >> Inputs we need from the user: << '''

# Total rent
# Persons living in room/flat
# Total food ordered for snaking
# Electricity units spended
# Change per Unit

''' >> Outputs: << '''

# Total amount to pay...

import time

user_rent = int(input("Provide the rent for the hostel or flat (per month): ")) 
persons_living = int(input("How many individuals are sharing the room/flat? "))
food_rent = int(input("What are the total food expenses? "))
electricity_spend = int(input("What is the total electricity expenditure? "))
charge_per_unit = int(input("Specify the cost of electricity per unit: "))

total_elec_bill = electricity_spend * charge_per_unit

print("\nGenerating the bill...")
time.sleep(3)

output = (user_rent + food_rent + total_elec_bill) // persons_living

print(f"\nEach person has to pay: {output} Rupees")