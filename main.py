import basic_fun
from accounts import employees, members

bank_open = True
while bank_open:
    ident = input('Hello! How would you like to access your account? By account number?')
    if ident == 'account number':
        acc_num = input('What is the account number?')
        pin = input('What is the PIN number for this account?')
        name = input('What is your name?')
        if pin != members[acc_num]['PIN']:
            print('This is not the correct PIN for this account')
        elif name not in members[acc_num]['Holder']:
            print('You are not an account holder for this account.')
        else:
            function = input('What would you like to do today? Deposit, withdraw, or transfer money? Or would you just like to check your balance? (D, W, T, C)')
            if function == 'D':
                amount = input('How much would you like to deposit?')
                print('You have $' + str(basic_fun.deposit(acc_num, amount) + ' left in your account now.')
            elif function == 'W':
                amount = input('How much would you like to withdraw?')
                print('You have $' + str(basic_fun.withdrawl(acc_num, amount)) + ' left in your account now.')
            elif function == 'T':
                destin = input('Where would you like to deposit money? Please tell me the account number.')
                amount = input('How much money would you like to deposit?')
                print('You have $' + str(basic_fun.transfer(acc_num, destin, amount, name)) + 'left in your account now.')