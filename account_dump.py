import random
import string


randomString = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))

accountsGenerated = [
    'test',
    'test2',
    'test3'
]

with open('accounts-'+randomString+'.txt', 'w') as accountsFile:
    for account in accountsGenerated:
        accountsFile.write(account+'\n')
