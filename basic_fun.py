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
	members[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers)')
    # while not validators.is_phone(members[acc_num]['Phone']):
    #     members[acc_num]['Phone'] = input('What is your 10-digit phone number? (Just numbers)')
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
    new = current - amount

    #If the account becomes negative, they will not be able to withdraw that amount
    if new < 0:
        print('Withdrawing this amount will result in a negative balance. Please deposit more money before requesting this amount again.')
        return current
    else:
        members[acc_num]['Balance'] = new
        print('You have successfully withdrawn $' + str(amount) + ' from your account.')
        return new

def deposit(acc_num, amount):
    members[acc_num]['Balance'] += amount
    print('You have successfully deposited $' + str(amount) + ' into your account.')
    return members[acc_num]['Balance']

def transfer(origin, destin, amount, name):
    if validators.is_holder(destin, name):
        members[destin]['Balance'] += amount
        members[origin]['Balance'] -= amount
        print('You have successfully transfered $' + str(amount) + ' into the account ending in ' + destin[6:] + '.')
        return members[origin]['Balance']
    print('You are not an account holder on the account ending in ' + destin[6:] + ' and cannot transfer money into this account.')
    return members[origin]['Balance']