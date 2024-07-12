# Program Description: A simple mortgage calculation program

import math
import time

# Define a constant for property tax rate
PROPERTY_TAX_RATE = 1.5

def main():
    # Variable declarations
    property_zip_code = ""
    property_address = ""
    property_offer_price = 0.0
    down_payment_percentage = 0.0
    annual_interest_rate = 0.0
    number_of_years_financing = 0
    loan_amount = 0.0
    monthly_interest_rate = 0.0
    monthly_mortgage_payment = 0.0
    monthly_property_tax = 0.0
    total_monthly_payment = 0.0
    total_payment = 0.0

    # Obtain user input
    property_zip_code = input("Enter property zip code: ")
    property_address = input("Enter property address: ")
    property_offer_price = float(input("Enter property offer price: $"))
    down_payment_percentage = float(input("Enter down payment (in percentage %): "))
    number_of_years_financing = int(input("Enter number of years financing: "))
    annual_interest_rate = float(input("Enter annual interest rate (in percentage %): "))

    # Pause the program to simulate a delay
    print("Mortgage calculator is processing your data ... Please wait …")
    time.sleep(3)  # sleep for 3 seconds

    # Perform loan calculations
    total_down_payment = property_offer_price * down_payment_percentage / 100
    loan_amount = property_offer_price - total_down_payment
    loan_maturity_date = "12/31/" + str(2023 + number_of_years_financing)
    monthly_interest_rate = annual_interest_rate / 1200
    monthly_mortgage_payment = loan_amount * monthly_interest_rate / (1 - 1 / math.pow(1 + monthly_interest_rate, number_of_years_financing * 12))
    monthly_property_tax = property_offer_price * PROPERTY_TAX_RATE / 100 / 12
    total_monthly_payment = monthly_mortgage_payment + monthly_property_tax
    total_payment = monthly_mortgage_payment * 12 * number_of_years_financing

    # Output the results
    print("\n")
    print("Property Zip Code: " + property_zip_code)
    print("Property Address: " + property_address)
    print(f"Property Offer Price: ${property_offer_price:.2f}")
    print(f"Down Payment: ${total_down_payment:.2f}")
    print(f"Loan Amount: ${loan_amount:.2f}")
    print("Loan Maturity Date: " + loan_maturity_date)
    print(f"Monthly Mortgage Payment: ${monthly_mortgage_payment:.2f}")
    print(f"Monthly Property Tax: ${monthly_property_tax:.2f}")
    print(f"Total Monthly Payment: ${total_monthly_payment:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")

if __name__ == "__main__":
    main()