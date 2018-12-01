import json, random, validators

def read():
	a = open('accounts.txt', 'r')
	accounts = json.loads(a.read())
	a.close()
	return accounts


def write(info):
	a = open('accounts.txt', 'w')
	a.write(json.dumps(info))
	a.close()


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
	accounts[acc_num]['Account'] = input('What type of account would you like to open? (C for Checking or S for Saving) ')
	
	#Defines account holders as a list mapped to the account key
	holder = []
	joint = input('Is this a joint account? (Y/N) ')
	if joint == 'Y':
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
	accounts[acc_num]['Account Alias'] = input('Give me an alias for the account. This is similar to a nickname for the account. ')
	
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


def check_balance(acc_num):
	accounts = read()
	return accounts[acc_num]['Balance']


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


def deposit(acc_num, amount):
	accounts = read()
	accounts[acc_num]['Balance'] += int(amount)
	print('You have successfully deposited $' + str(amount) + ' into your account.')
	
	write(accounts)
	return accounts[acc_num]['Balance']


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


def transactions_occur(acc_num):
	customer = True
	while customer:
		function = input('What would you like to do to day? Check your balance, deposit, withdraw, or transfer money? (C, D, W, T) ')
		
		if function == 'D':
			amount = input('How much would you like to deposit? ')
			print('You have $' + str(deposit(acc_num, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		elif function == 'W':
			amount = input('How much would you like to withdraw? ')
			print('You have $' + str(withdrawl(acc_num, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		elif function == 'T':
			destin = input('Where would you like to deposit money? Please tell me the account number. ')
			amount = input('How much money would you like to deposit? ')
			print('You have $' + str(transfer(acc_num, destin, amount)) + ' left in your account now.')
			transaction = input('Would you like to make another transaction? (y/n) ')
		elif function == 'C':
			print('You have $' + str(check_balance(acc_num)) + ' in your account.')
			transaction = input('Would you like to make another transaction? (y/n) ')

		#Decides whether or not another transaction is to be made
		if transaction == 'y':
			customer = True
		else:
			print('''
			Thank you for banking with us today!
			''')
			customer = False


def get_aliases(name):
	accounts = read()

	#Populates a list of that holder's account aliases
	aliases = [accounts[acc_num]['Account Alias'] for acc_num in accounts if name in accounts[acc_num]['Holder']]

	return aliases


def find_account(alias, name):
	accounts = read()

	#Finds accounts with the alias in question
	acct_with_alias = [acc_num for acc_num in accounts if alias in accounts[acc_num]['Account Alias']]

	#Finds accounts with the holder listed
	for acct in acct_with_alias:
		if name in accounts[acct]['Holder']:
			return acct
	
	#Note: Technically, it is possible for the name to not be listed under any of the accounts; however, since this will only be called after we have established that they are a holder of an account with that alias, we shouldn't encounter that error