import basic_fun

#Gets all aliases in use by that holder
def get_aliases(name):
	accounts = basic_fun.read()

	#Populates a list of that holder's account aliases
	aliases = [accounts[acc_num]['Account Alias'] for acc_num in accounts if name in accounts[acc_num]['Holder']]

	return aliases


#Finds account based on alias and name
def find_account(alias, name):
	accounts = basic_fun.read()

	#Finds accounts with the alias in question
	acct_with_alias = [acc_num for acc_num in accounts if alias in accounts[acc_num]['Account Alias']]

	#Finds accounts with the holder listed
	for acct in acct_with_alias:
		if name in accounts[acct]['Holder']:
			return acct
	
	#Note: Technically, it is possible for the name to not be listed under any of the accounts; however, since this will only be called after we have established that they are a holder of an account with that alias, we shouldn't encounter that error


#Calculates what the balance should be after interest is added
def add_interest(acc_num):
    accounts = basic_fun.read()
    percent = accounts[acc_num]['Balance'] * .02
    accounts[acc_num]['Balance'] += percent
    return accounts[acc_num]['Balance']


#Applies interest to savigns accounts
def do_interest():
    accounts = basic_fun.read()

    #Populates a list of savigns accounts
    savings = [acc_num for acc_num in accounts if accounts[acc_num]['Account'] == 'S']
    
    #Adding the interest
    for acct in savings:
        new = add_interest(acct)
        accounts[acct]['Balance'] = new

    basic_fun.write(accounts)


#Gets a list of account holders
def get_holders():
    accounts = basic_fun.read()
    
    holders = [name for num in accounts for name in accounts[num]['Holder']]

    return holders


#Gets a list of aliases used by all account holders on one accounts
def is_holder(holders):
    members = get_holders()

    aliases = []
    for name in holders:
        if name in members:
            name_alias = get_aliases(name)
            for alias in name_alias:
                aliases.append(alias)

    return aliases