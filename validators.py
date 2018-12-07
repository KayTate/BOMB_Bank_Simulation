import datetime, helpers, basic_fun

#Catches same-account transfers
def is_same(origin, destin):
    if origin == destin:
        return True
    return False

#Catches invalid phone numbers
def is_phone(number):
    if len(number) != 10:
        print('This is not a valid 10-digit number.')
        return False
    for char in number:
        if char not in '1234567890':
            print('This is not a valid 10-digit number.')
            return False
    return True

#Age Validator
def is_adult(year):
    #Makes sure its a number:
    for char in str(year):
        if char not in '1234567890':
            return False
    
    #Gets the current year
    now = datetime.datetime.now()
    cyear = now.year

    #Checks age
    age = cyear-year
    if age < 18:
        return False
    return True

#Valid dollar amount
def is_dollar(amount):
    for char in str(amount):
        if char not in '1234567890':
            return False
    return True

#Checks to see if account number is an account
def is_account(number):
    accounts = basic_fun.read()
    if number not in accounts:
        return False
    return True