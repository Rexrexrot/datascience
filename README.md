# datascience

Python Script for Data Cleansing of E.ON Signup data

Please use the following script to solve data quality issues :

- Missing "Bundesland" information (9 percent of the records)
- Leading zeros in postcode is missing when lenght is 4 digits
- Delete ".0" in postcode
- Drop wrong product names

Input files:
- postcode_txt.txt
- Interview_signup_.csv

# Data description, input file Interview_signup_.csv :

o	 original_product_name: Product the customer signed up to
o	 postcode: Postcode of the customer (5 digits with 0-9)
o	 bundesland: The state the customer lives
o	 total_bonus: The bonus amount we provided (reduces the first year price)
o	 order_date: The date that the customer ordered the product

# Data description, input file postcode_txt.txt :

o	 postcode: postcode as 5 digit number
o	 Bundesland as text

Output files
- eon challenge final.py     ... Python script for data cleansing
- interview_signup_fin.csv   ... final result file

