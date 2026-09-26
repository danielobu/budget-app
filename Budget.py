class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description= ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description })
            return True
        return False

    def get_balance(self):
        return sum(item['amount']for item in self.ledger)

    def transfer(self,amount, other_category):
        if self.check_funds(amount):
            
            self.withdraw(amount, f'Transfer to {other_category.name}')

            other_category.deposit(amount, f'Transfer from {self.name}')
            
            return True
        return False 

    def check_funds(self,amount):
        total_amount = sum(item['amount']for item in self.ledger)

        if amount > total_amount:
            return False
        return True

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        item_string = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            item_string += f"{desc:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + item_string + total


def create_spend_chart(categories):
    spent = []
    for category in categories:
        s = 0
        for item in category.ledger:
            if item['amount'] < 0:
                s += abs(item['amount'])
        spent.append(s)

    total_spent = sum(spent)
    percentage = []

    for s in spent:
        if total_spent == 0:
            percentage.append(0)

        else:
            pct = int((s/total_spent)*100//10)*10
            percentage.append(pct)

def create_spend_chart(categories):
    spent = []
    for category in categories:
        s = 0
        for item in category.ledger:
            if item['amount'] < 0:
                s += abs(item['amount'])
        spent.append(s)

    total_spent = sum(spent)
    percentage = []

    for s in spent:
        if total_spent == 0:
            percentage.append(0)
        else:
            pct = int((s / total_spent) * 100 // 10) * 10
            percentage.append(pct)

    chart = "Percentage spent by category\n"

    # 1. Build Y-Axis and Bars
    for i in range(100, -10, -10):
        chart += f'{i:3}| ' 
        for pct in percentage:
            if pct >= i:
                chart += 'o  '
            else:
                chart += '   '

        chart += '\n'

    # 2. Fixed Dashed Line (4 spaces + solid hyphens)
    dash_line = "    " + "-" * (len(categories) * 3 + 1) + "\n"
    chart += dash_line

    # 3. Build Vertical Category Names
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            # Fixed: Use 'i' instead of the undefined 'row'
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
            
        if i < max_length - 1:
            chart += '\n'

    return chart


food = Category('food')      

food.deposit(2000, 'initial deposit')

food.withdraw(50.5, 'groceries')

food.transfer(100, Category('clothing'))

print(food)








    




        
    
