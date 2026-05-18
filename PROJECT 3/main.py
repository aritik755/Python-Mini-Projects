## INPUT FORM THE USERS
# TOTAL RENT 
# TOTAL FOOD ORDERED 
# ELECTRICITY BILL 
# CHARGE/UNIT 
# NO. OF PERSONS LIVING IN THE ROOM/FLAT 

## OUTPUT 
# TOTAL AMOUNT TO PAY 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge/unit = "))
persons = int(input("Enter the number of persons in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay =", output)