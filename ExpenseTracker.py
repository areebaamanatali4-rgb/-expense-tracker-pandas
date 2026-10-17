
import pandas as pd

# Taking input for expenses
n = int(input("Enter number of expenses = "))

category = []
value = []

for i in range(n):
    category1 = input("Enter expense category = ")
    value1 = int(input("Enter expense amount = "))

    category.append(category1)
    value.append(value1)

# Creating a DataFrame
df = pd.DataFrame({
    "Category": category,
    "Value": value
})

print("\nExpense Details")
print(df)

# Calculating expense summary
total = df["Value"].sum()
average = round(df["Value"].mean(), 2)
maximum = df["Value"].max()
minimum = df["Value"].min()

print("\nTotal expenses =", total)
print("Average expense =", average)
print("Maximum expense =", maximum)
print("Minimum expense =", minimum)

# Taking input for budget
budget = int(input("\nEnter your budget = "))

# Checking budget and calculating percentage
if budget <= 0:
    print("Budget must be greater than zero.")

else:
    if total < budget:
        remaining = budget - total
        print(f"You are within budget. Rs. {remaining} left.")

    elif total > budget:
        extra = total - budget
        print(f"Budget exceeded by Rs. {extra}.")

    else:
        print("Your budget is fully used.")

    percentage = round((total / budget) * 100, 2)
    print(f"You have used {percentage}% of your budget.")

# Sorting expenses from highest to lowest
sorted_expenses = df.sort_values("Value", ascending=False)

print("\nExpenses from highest to lowest:")
print(sorted_expenses)
