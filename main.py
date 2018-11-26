import json

my_d  = {
    '1234567890' : ['C','Olivia Asemota', '1234567890', '123 Pine St', '1234', 5000]
}

save = open('accounts.txt', 'w')
save.write(json.dumps(my_d))
save.close()