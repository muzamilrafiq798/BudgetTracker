
print("\n____Budget Tracker____")
#Total user input
Total_Pay = int(input("Enter your total pay: "))
Total_uni_fee = int(input("Enter your total uni fee: "))

#Expense dictionary
expenses = {
    "Monthly Fee":0,
    "Flat rent":0,
    "Grocery":0,
    "Travel expense":0,
    "Mobile installment":0,
    "Other(misc)":0,
}

for key in expenses:
    expenses[key] = int(input("Enter " + key + " amount: "))

#Calculation
print("\n____Budget Tracker____")
print(expenses)
Total_Monthly_Expense = sum(expenses.values())
print("Total Monthly Expense = ", Total_Monthly_Expense,"pounds")
Savings = Total_Pay - Total_Monthly_Expense
print("Total Savings = ", Savings,"pounds")
Remaining_uni_fee = Total_uni_fee - expenses["Monthly Fee"]
print("Remaining uni fee = ", Remaining_uni_fee,"pounds")