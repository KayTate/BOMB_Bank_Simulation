import json, random, validators, helpers

#Handles text files
def read():
	a = open('accounts.txt', 'r')
	accounts = json.loads(a.read())
	a.close()
	return accounts
def write(info):
	a = open('accounts.txt', 'w')
	a.write(json.dumps(info))
	a.close() 


#Opens Accounts
def open_acc():
	#Loads account dictionary
	accounts = read()

	#Randomly generates a 10-digit number to act as the account number
	acc_num = str(random.randint(1000000000,10000000000))
	#Ensures that each account number is unique
	while acc_num in accounts:
		acc_num = str(random.randint(1000000000,10000000000))
		
	accounts[acc_num] = {}
	
	#Defines account type
	acc_type = input('What type of account would you like to open? (C for Checking, S for Saving, or B for Business) ')
	acc_type.capitalize()
	while acc_type not in 'CSB':
		acc_type = input('Please tell me a valid account type: C for Checking, S for Saving, or B for Business')
	accounts[acc_num]['Account'] = acc_type

	#Defines account holders as a list mapped to the account key
	holder = []
	joint = input('Is this a joint account? (Y/N) ')
	while joint not in 'YyNn':
		joint = input('Please tell me if this is a joint account. Y for yes, N for no.')
	if joint in 'Yy':
		name = input('What is one name on the account? ')
		holder = [name]
		while name != 'n':
			name = input('What is the next name on the account? Enter "n" when there are no more account holders. ')
			if name != 'n':
				holder.append(name)
	else:
		name = input('What is the name on the account? ')
		holder = [name]
	accounts[acc_num]['Holder'] = holder
	
	#Asks for arbitrary phone number and address
	accounts[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers) ')
	while not validators.is_phone(accounts[acc_num]['Phone']):
		accounts[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers) ')
	accounts[acc_num]['Address'] = input('What is your address? ')
	
	#Creates account alias:
	aliases = helpers.is_holder(holder)
	alias = input('Give me an alias for the account. This is similar to a nickname for the account. ')
	while alias in aliases:
			alias = input('You already have an account with that alias. Please give me a new one.')
	accounts[acc_num]['Account Alias'] = alias
	
    #Creates PIN number
	pin = str(random.randint(1000,10000))
	accounts[acc_num]['PIN'] = pin
	print('Your account number is ' + acc_num + ' and your Personalized Identification Number is ' + pin + '. You will need this information to access your account in the future.')
	
	#Sets balance to 0
	accounts[acc_num]['Balance'] = 0

	#Saves account information back to text file
	accnts = open('accounts.txt', 'w')
	accnts.write(json.dumps(accounts))
	accnts.close()


#Checks balances
def check_balance(acc_num):
	accounts = read()
	return accounts[acc_num]['Balance']


#Withdraws money
def withdrawl(acc_num, amount):
	accounts = read()
	current = check_balance(acc_num)
	new = current - int(amount)
	
	#If the account becomes negative, they will not be able to withdraw that amount
	if new < 0:
		print('Withdrawing this amount will result in a negative balance. Please deposit more money before requesting this amount again.')
		return current
	else:
		accounts[acc_num]['Balance'] = new
		print('You have successfully withdrawn $' + str(amount) + ' from your account.')
		write(accounts)
		return new


#Deposits money
def deposit(acc_num, amount):
	accounts = read()
	accounts[acc_num]['Balance'] += int(amount)
	print('You have successfully deposited $' + str(amount) + ' into your account.')
	
	write(accounts)
	return accounts[acc_num]['Balance']


#Transfers money
def transfer(origin, destin, amount):
	accounts = read()
	if validators.is_same(origin, destin):
		print('You cannot transfer money to the original account')
		return accounts[origin]['Balance']
	accounts[destin]['Balance'] += int(amount)
	accounts[origin]['Balance'] -= int(amount)
	print('You have successfully transfered $' + str(amount) + ' into the account ending in ' + destin[6:] + '.')
	write(accounts)
	return accounts[origin]['Balance']


#Closes account
def close_acct():
	accounts = read()

	confirm = input('''
	Are you sure you would like to close your account?
	Y for Yes, N for No
	''')
	while confirm not in 'YyNn':
		confirm = input('Please tell me whether or not you would like to close your account...Y for yes, N for no. ')

	if confirm in 'Nn':
		print('Thank you for staying with us. Have a great day!')
	else:
		acc_num = input('''
		We are sorry to lose you today!
		What is your account number?
		''')
		phone = input('''
		For safety purposes, we will need you to confirm all of the information in your account.
		Can you get us the phone number on the account? ''')
		address = input('''
		The address for the account? ''')
		alias = input('''
		The account alias? ''')
		balance = int(input('''
		The balance on the account? '''))
		name = input('''
		Your name? ''')
		pin = input('''
		And finally the PIN on the account? ''')

		if (phone != accounts[acc_num]['Phone'] or address != accounts[acc_num]['Address'] or alias != accounts[acc_num]['Account Alias'] or balance != int(accounts[acc_num]['Balance']) or pin != accounts[acc_num]['PIN'] or name not in accounts[acc_num]['Holder']):
			print('''I'm sorry; some of the information you have given me is incorrect and I will not be able to close your account today.''')

		else:
			accounts.pop(acc_num)
			print('''Your account has been closed. Have a great day.''')
			write(accounts)


#Function call for all transaction functions (except close account)
def transactions_occur(acc_num):
	customer = True
	while customer:
		function = input('What would you like to do today? Check your balance, deposit, withdraw, or transfer money? (C, D, W, T) ')
		
		while function not in 'CcDdWwTt':
			function = input('Please tell me what you would like to do today. Check your balance, deposit, withdraw, or transfer money? (C, D, W, T) ')

		if function in 'dD':
			amount = input('How much would you like to deposit? ')
			while not validators.is_dollar(amount):
				amount = input('Please tell me a valid numeric value.')
			print('You have $' + str(deposit(acc_num, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		elif function in 'wW':
			amount = input('How much would you like to withdraw? ')
			while not validators.is_dollar(amount):
				amount = input('Please tell me a valid numeric value.')
			print('You have $' + str(withdrawl(acc_num, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		elif function in 'tT':
			destin = input('Where would you like to deposit money? Please tell me the account number. ')
			while not validators.is_account(destin):
				destin = input('Please enter a valid destination account number. The one you gave me does not belong to an account here.')
			amount = input('How much money would you like to deposit? ')
			while not validators.is_dollar(amount):
				amount = input('Please tell me a valid numeric value.')
			print('You have $' + str(transfer(acc_num, destin, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		else:
			print('You have $' + str(check_balance(acc_num)) + ' in your account.')
			transaction = input('Would you like to make another transaction? (y/n) ')

		#Decides whether or not another transaction is to be made
		while transaction not in 'yYNn':
			transaction = input('''
			Can you repeat yourself? 
			Would you like to make another transaction?
			(Y/N)
			''')
		if transaction in 'Yy':
			customer = True
		else:
			print('''
			Thank you for banking with us today!
			''')
			customer = False


#Pays the tellers
def payment():
	# Handle text files
	e = open('employees.txt', 'r')
	employees = json.loads(e.read())
	e.close()

	a = open('accounts.txt','r')
	accounts = json.loads(a.read())
	a.close()

	#Creates dictionary mapping the employee to their employee account number
	emp_accounts = {}
	for account in accounts:
		if accounts[account]['Account'] == 'E':
			name = accounts[account]['Holder'][0]
			emp_accounts[name] = account

	#Calculates check and adds payment
	for employee in employees:
		hours = employees[employee]['Hours']
		wage = employees[employee]['Wage']
		check = hours * wage
		accounts[emp_accounts[employee]]['Balance'] += check
		employees[employee]['Hours'] = 0

	#Saves files
	e = open('employees.txt','w')
	e.write(json.dumps(employees))
	e.close()

	a = open('accounts.txt','w')
	a.write(json.dumps(accounts))
	a.close()

	return employees