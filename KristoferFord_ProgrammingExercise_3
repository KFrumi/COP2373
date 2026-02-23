from functools import reduce

# Function to get user input for expenses
def get_expenses():
    """Function to prompt the user for their monthly expenses and store them
    in a list of tuples with (expense_type, expense_amount).

    Returns:
        expenses (list): A list of tuples with expense type and amount."""
    expenses = []
    while True:
        # Get type of expense
        expense_type = input("Enter the expense type (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break

        # Get the amount for the expense
        try:
            expense_amount = float(input(f"Enter the amount for {expense_type}: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue
        
        expenses.append((expense_type, expense_amount))
    return expenses


# Function to calculate the total, highest, and lowest expenses
def calculate_expenses(expenses):
    
    """Function to calculate the total, highest, and lowest expenses from a list of expenses.

    Parameters:
        expenses (list): A list of tuples with expense type and amount.

    Returns:
        total_expense (float): The sum of all expenses.
        highest_expense (tuple): The expense with the highest amount (type, amount).
        lowest_expense (tuple): The expense with the lowest amount (type, amount)."""
    # Use reduce to calculate the total expense
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    # Use the max and min functions to find the highest and lowest expenses
    highest_expense = max(expenses, key=lambda x: x[1])
    lowest_expense = min(expenses, key=lambda x: x[1])

    return total_expense, highest_expense, lowest_expense


# Function to display the results
def display_results(total_expense, highest_expense, lowest_expense):
    
    """Function to display the results of the expense calculations.

    Parameters:
        total_expense (float): The total of all expenses.
        highest_expense (tuple): The expense with the highest amount.
        lowest_expense (tuple): The expense with the lowest amount."""
        
    print("\nExpense Summary:")
    print(f"Total expense: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} (${highest_expense[1]:.2f})")
    print(f"Lowest expense: {lowest_expense[0]} (${lowest_expense[1]:.2f})")


# Main function to run the program
def main():
    """Main function to run the program. It coordinates the process of getting expenses,
    calculating totals, and displaying results."""
    expenses = get_expenses()
    if expenses:
        total_expense, highest_expense, lowest_expense = calculate_expenses(expenses)
        display_results(total_expense, highest_expense, lowest_expense)
    else:
        print("No expenses were entered.")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
    