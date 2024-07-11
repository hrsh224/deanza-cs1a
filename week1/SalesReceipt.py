"""
File Name: SalesReceipt.py
Program Description: In-n-Out Burger Sales Receipt Program
Author: Harish Allamraju
Revision History:
- First implementation (July 10, 2024)
"""

# Declare variables
guest_number = 0
store_location = ""
cashier_name = ""
counter_take_out = 0.0
amount_due = 0.0

# Assign values
guest_number = 21
store_location = "LINQ"
cashier_name = "STEPHEN KYLE MA"
counter_take_out = 12.65
amount_due = 13.71
shake = 2.75

# Output sales receipt
print("\t\t\tYOUR GUEST NUMBER IS")
print("\t\t\t\t", guest_number)

print("\t\t\tIN-N-OUT BURGER", store_location)
print("------------------------------------------------------")
print("Cashier:", cashier_name)
print("Check:", guest_number)
print("------------------------------------------------------")
print(f"2 Dbl-Dbl\t\t   {9.90:.2f}")
print("1 Reg Chocolate Shk\t  ", shake)
print("COUNTER - Take Out\t$", counter_take_out)
print("TAX 8.375%\t\t  ", 1.06)
print("Amount Due\t\t$", amount_due)