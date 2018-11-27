import basic_fun
from accounts import employees, members

bank_open = True 
while bank_open:
    have_acct = input('Hello! Do you have an account with us? (y/n) ')

    #Opens account
    if have_acct == 'n':
        #Current options: yes, no
        #Future options: build-your-own-adventure key words
        ident = input('Would you like to open an account with us today? (y/n) ')
        if ident == 'y':
            basic_fun.open_acc()
            new_trans = input('Would you like to complete more transactions? (y/n) ')
            if new_trans == 'y': 
                acc_num = input('For security purposes, please give me the account number for the account you just created. ')
                basic_fun.transactions_occur(acc_num)

    #Requests identification to locate account
    elif have_acct == 'y':
        #Current options: account number
        #Future options: name, build-your-own-adventure key words
        ident = input('How would you like to access your account? By account number? ')
        
        #Enters account based on account number
        if ident == 'account number':
            acc_num = input('What is the account number? ')
            pin = input('What is the PIN number for this account? ')
            name = input('What is your name? ')

            #Decides whether or not the user has access to the account
            if pin != members[acc_num]['PIN']:
                print('This is not the correct PIN for this account')
                customer = False
            elif name not in members[acc_num]['Holder']:
                print('You are not an account holder for this account.')
                customer = False
            
            #Transactions occur until the user is done
            else:
                basic_fun.transactions_occur(acc_num)

    #Determines if another customer is ready to be served; hopefully will be replaced with timery
    bank_open = input('Is the bank still open? (y/n) ')
    if bank_open == 'y':
        bank_open = True
    else:
        bank_open = False