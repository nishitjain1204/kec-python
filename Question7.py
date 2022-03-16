# 7. Find my Financial year (FY)
# Help a tax consultant sort out his invoices based on the invoice date (dd-mm-yyyy format) into it's
# respective FY.
# Tip: A FY is a 1 year accounting period between 1st April of one year to 31st March of consecutive
# year.
# Eg: FY: 2020-2021 means the invoices dated between 01-04-2020 to 31-03-2021.
# Example:
# Input: 03-03-2021
# Output: FY: 2020-2021

import datetime

input_date = datetime.datetime.strptime(input(), "%d-%m-%Y").date()

pres_year = input_date.year
# print(type(pres_year))

if input_date < datetime.datetime.strptime("01-04-"+str(pres_year),"%d-%m-%Y").date():
    print(f"{pres_year-1} - {pres_year}") 
else:
    print(f"{pres_year} - {pres_year+1}")
    
