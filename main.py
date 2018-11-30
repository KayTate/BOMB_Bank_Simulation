import json, time, basic_fun, hiring, robbery

start = time.time()

e = open('employees.txt', 'r')
employees = json.loads(e.read())
e.close()

a = open('accounts.txt', 'r')
accounts = json.loads(a.read())
a.close()

bank_open = True 
while bank_open:
    #Entrance for BYOA stories
    #Hiring Story: I would like a job
    #Robbery Story: Hands up
    have_acct = input('Hello! How can I help you today? Do you have an account with us? (y/n) ')

    #Opens account
    if have_acct == 'n':
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
        #Future options: name
        ident = input('How would you like to access your account? By account number? ')
        
        #Enters account based on account number
        if ident == 'account number':
            acc_num = input('What is the account number? ')
            pin = input('What is the PIN number for this account? ')
            name = input('What is your name? ')

            #Decides whether or not the user has access to the account
            if pin != accounts[acc_num]['PIN']:
                print('This is not the correct PIN for this account')
            elif name not in accounts[acc_num]['Holder']:
                print('You are not an account holder for this account.')
            
            #Transactions occur until the user is done
            else:
                basic_fun.transactions_occur(acc_num)

    #Hiring BYOA
    elif have_acct == 'I would like a job':
        hiring.hiring_story()

    #Robbery BYOA
    elif have_acct == 'Hands up':
        robbery.robbery_story()

    #Determines if the bank is still open; runs for 5 minutes
    if time.time() - start > 300:
        bank_open = False