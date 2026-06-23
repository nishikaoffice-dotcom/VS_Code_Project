#Program to read number from the input excel file and write it into output excel file 
import pandas as pd

# Step 1: Read numbers from Excel file
data = pd.read_excel("input.xlsx")   # assumes numbers are in first column 

# Step 2: Create a new column with Even/Odd labels
def check_even_odd(num):
    if isinstance(num, int):
        if num % 2 == 0:
            return "Even" 
        else:
             return "Odd"    
    else:
        return "Invalid"

# data.iloc is used to select the first column of the excel sheet
data["Result"] = data.iloc[:,0].apply(check_even_odd)  

# Step 3: Write results into a new Excel file
data.to_excel("output.xlsx", index=False)

print("✅ Processing complete! Results saved in output.xlsx")
