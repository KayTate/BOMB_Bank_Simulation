from accounts import members, employees
import validators
import random


def open_acc():
	#Randomly generates a 10-digit number to act as the account number
	acc_num = str(random.randint(1000000000,10000000000))
	#Ensures that each account number is unique
	while acc_num in members:
		acc_num = str(random.randint(1000000000,10000000000))
		
	members[acc_num] = {}
	
	#Defines account type
	members[acc_num]['Account'] = input('What type of account would you like to open? (C for Checking or S for Saving) ')
	
	#Defines account holders as a list mapped to the account key
	holder = []
	joint = input('Is this a joint account? (Y/N) ')
	if joint == 'Y':
		name = input('What is one name on the account? ')
		holder = [name]
		while name != 'n':
			name = input('What is the next name on the account? Enter "n" when there are no more account holders. ')
			holder.append(name)
	else:
		name = input('What is the name on the account? ')
		holder = [name]
	
	#Asks for arbitrary phone number and address
	members[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers) ')
	while not validators.is_phone(members[acc_num]['Phone']):
		members[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers) ')
	members[acc_num]['Address'] = input('What is your address? ')
    
    #Creates PIN number
	pin = str(random.randint(1000,10000))
	members[acc_num]['PIN'] = pin
	print('Your account number is ' + acc_num + ' and your Personalized Identification Number is ' + pin + '. You will need this information to access your account in the future.')
	
	#Sets balance to 0
	members[acc_num]['Balance'] = 0

def check_balance(acc_num):
    return members[acc_num]['Balance']

def withdrawl(acc_num, amount):
    current = check_balance(acc_num)
    new = current - int(amount)

    #If the account becomes negative, they will not be able to withdraw that amount
    if new < 0:
        print('Withdrawing this amount will result in a negative balance. Please deposit more money before requesting this amount again.')
        return current
    else:
        members[acc_num]['Balance'] = new
        print('You have successfully withdrawn $' + str(amount) + ' from your account.')
        return new

def deposit(acc_num, amount):
    members[acc_num]['Balance'] += int(amount)
    print('You have successfully deposited $' + str(amount) + ' into your account.')
    return members[acc_num]['Balance']

def transfer(origin, destin, amount):
	if validators.is_same(origin, destin):
		print('You cannot transfer money to the original account')
		return members[origin]['Balance']
	members[destin]['Balance'] += int(amount)
	members[origin]['Balance'] -= int(amount)
	print('You have successfully transfered $' + str(amount) + ' into the account ending in ' + destin[6:] + '.')
	return members[origin]['Balance']

def transactions_occur(acc_num):
	customer = True
	while customer:
		function = input('What would you like to do to day? Check your balance, deposit, withdraw, or transfer money? (C, D, W, T)')
		
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
			customer = False