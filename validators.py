from accounts import employees, members

def is_holder(acc_num, name):
    for holder in members[acc_num]['Holder']:
        if name == holder:
            return True
    return False

def is_phone(number):
    if len(number) != 10:
        print('This is not a valid 10-digit number.')
        return False
    for char in number:
        if char not in '1234567890':
            print('This is not a valid 10-digit number.')
            return False
    return True