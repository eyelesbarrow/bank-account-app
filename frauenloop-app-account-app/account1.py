

user_data = {'user1': ['1234', 2000], 'user2': ['5576', 3000], 'user3': ['2293', 200]}

class Account:

    def __init__(self, pin_number, user_name):
        self.pin_number = pin_number
        self.user_name = user_name


    def display_balance(self, pin_number, user):
        if pin_number == user_data[user][0]:
            interest_rate = 0
            interest_rate += 1
            return 'This is your current balance: {} EUR'.format(user_data[user][1])
        else:
            return pin_error()

    def pin_error(self):
        return 'Access denied: incorrect PIN.'

    # print(display_balance(1234, 'user1'))

    def withdraw_money(self, pin_number, user_name, amount):
        balance = user_data[user_name][1]
        if pin_number == user_data[user_name][0]:
            if amount <= balance:
                balance = balance - amount
                return 'Withdrew {} EUR. New balance is: {} EUR.'.format(amount, balance)
            else:
                return 'You are not allowed to withdraw more money than you have on your account!'
        else:
            return pin_error()

