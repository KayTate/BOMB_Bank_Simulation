import basic_fun

def get_aliases(name):
	accounts = basic_fun.read()

	#Populates a list of that holder's account aliases
	aliases = [accounts[acc_num]['Account Alias'] for acc_num in accounts if name in accounts[acc_num]['Holder']]

	return aliases


def find_account(alias, name):
	accounts = basic_fun.read()

	#Finds accounts with the alias in question
	acct_with_alias = [acc_num for acc_num in accounts if alias in accounts[acc_num]['Account Alias']]

	#Finds accounts with the holder listed
	for acct in acct_with_alias:
		if name in accounts[acct]['Holder']:
			return acct
	
	#Note: Technically, it is possible for the name to not be listed under any of the accounts; however, since this will only be called after we have established that they are a holder of an account with that alias, we shouldn't encounter that error

def add_interest(acc_num):
    accounts = basic_fun.read()
    percent = accounts[acc_num]['Balance'] * .02
    accounts[acc_num]['Balance'] += percent
    return accounts[acc_num]['Balance']

def do_interest():
    accounts = basic_fun.read()

    #Populates a list of checking accounts
    savings = [acc_num for acc_num in accounts if accounts[acc_num]['Account'] == 'S']
    
    #Adding the interest
    for acct in savings:
        new = add_interest(acct)
        accounts[acct]['Balance'] = new

    basic_fun.write(accounts)