import json, time, random, basic_fun, hiring, robbery, complaint, stock, validators, helpers

start = time.time()

e = open('employees.txt', 'r')
employees = json.loads(e.read())
e.close()

a = open('accounts.txt', 'r')
accounts = json.loads(a.read()) 
a.close()

#Selects Employee
emp = list(employees.keys())
employee = random.choice(emp)

bank_open = True
while bank_open:
    #Entrance for BYOA stories
    #Hiring Story: I would like a job
    #Robbery Story: I want the money
    #"Can I speak to the manager?" Story: Where is your manager
    #Close bank early: Close
    #Pay tellers: Payment
    #Close Account: I would like to close my account
    print('Hello! My name is ' + employee + ', how can I help you today?')
    have_acct = input('''
    Would you like to speak to a trade specialist (T) or enter an account (Y/N)?
    ''')

    #Opens account
    if have_acct in 'nN':
        ident = input('Would you like to open an account with us today? (y/n) ')
        if ident in 'Yy':
            #Asks for and verifies age
            year = int(input('What year were you born in? '))
            if not validators.is_adult(year):
                print('Unfortunantly, you are too young to hold this account. You must be 18 or older.')
            else:
                basic_fun.open_acc()
                new_trans = input('Would you like to complete more transactions (y/n) ')
                if new_trans in 'Yy':
                    acc_num = input('For security purposes, please give me the account number for the account you just created. ')
                    basic_fun.transactions_occur(acc_num)
                else:
                    print('''
                    Thank you for banking with us today!
                    ''')
        else:
            print('''
            Have a good day
            ''')

    #Requests identification to locate account
    elif have_acct in 'yY':
        #Current options: account number
        #Future options: name
        ident = input('How would you like to access your account? By account number or alias? ')
        
        while ident not in ['account number', 'alias']:
            ident = input('''
            Please give me valid input
            How would you like to access your account? By account number or alias? 
            ''')

        #Enters account based on account number
        if ident == 'account number':
            acc_num = input('What is the account number? ')
            pin = input('What is the PIN number for this account? ')
            name = input('What is your name? ')

            #Decides whether or not the user has access to the account
            if pin != accounts[acc_num]['PIN']:
                pin = input('''
                This is not the correct PIN for this account. Please try again
                ''')
            elif name not in accounts[acc_num]['Holder']:
                print('You are not an account holder for this account.')
            
            #Transactions occur until the user is done
            else:
                basic_fun.transactions_occur(acc_num)

        #Enters the account based on alias and holder name
        elif ident == 'alias':
            #Gets name and possible aliases
            name = input('What is your name? ')

            aliases = helpers.get_aliases(name)
            print(aliases)
            alias = input('''
            These are the bank accounts we have for you. Which would you like to enter?
            Please give me the full alias (capitalization matters).
            ''')
            while alias not in aliases:
                alias = input('''
                That was not a suggested alias. Please give me a valid alias.
                ''' )

            #Gets account number and PIN
            acc_num = helpers.find_account(alias, name)
            pin = input('What is the PIN for this account? ')

            #Decides whether this is the correct PIN for the account
            if pin != accounts[acc_num]['PIN']:
                print('This is not the correct PIN for this account.')

            #Transactions occur
            else:
                basic_fun.transactions_occur(acc_num)


    #Hiring BYOA
    elif have_acct == 'I would like a job':
        hiring.hiring_story()

    #Robbery BYOA
    elif have_acct == 'I want the money': 
        robbery.robbery_story()

    #Manager BYOA
    elif have_acct == 'Where is your manager':
        complaint.complaint_to_man()

    #Early closing
    elif have_acct == 'Close':
        bank_open = False
        print('''
        We have closed early today.
        ''')

        #Adds hours and interest
        employees[employee]['Hours'] += int(((time.time() - start) // 60))
        helpers.do_interest()

    #Pay tellers
    elif have_acct == 'Payment':
        employees = basic_fun.payment()
        print('''The tellers have been paid''')

    #Closes account
    elif have_acct == 'I would like to close my account':
        basic_fun.close_acct()


    #Speak to Trade Specialist
    elif have_acct in 'Tt':
        stock.trader()


    #Catches other input
    else:
        print('''I'm sorry...we don't do that here.''')

    #Determines if the bank is still open; runs for 10 minutes
    if time.time() - start > 600:
        bank_open = False
        print('''
        Unfortunantly, we are closed for the day. Come back tomorrow!
        ''')

        #Changes the hours for the employee
        employees[employee]['Hours'] += 10

        #Gives checking accounts their interest 
        helpers.do_interest()

e = open('employees.txt', 'w')
e.write(json.dumps(employees))
e.close()