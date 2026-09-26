# Python Budget App

A robust object-oriented programming (OOP) project built in Python to manage personal finances, track transaction ledgers, handle secure account transfers, and generate text-based spending charts.

## Features

- **Category Management**: Create distinct budget categories (such as Food, Clothing, and Entertainment).
- **Transaction Ledger**: Automatically records deposits and withdrawals with custom descriptions.
- **Fund Validation**: Built-in balance checks to prevent overdrawing accounts.
- **Account Transfers**: Safely transfer funds between categories while updating both ledgers.
- **Visual Spend Chart**: Generates an ASCII percentage bar chart illustrating spending distribution across categories.

## Code Structure

- **`Category` Class**: Handles individual category creation, ledger entries, balance calculation, and formatted receipt strings (`__str__`).
- **`create_spend_chart(categories)` Function**: Calculates total category expenses and maps out a visual percentage breakdown from 0% to 100%.

## Example Usage

```python
food = Category('food')
food.deposit(1000, 'initial deposit')
food.withdraw(50.50, 'groceries')

clothing = Category('clothing')
food.transfer(100, clothing)

print(food)