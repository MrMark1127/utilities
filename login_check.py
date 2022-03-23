import os # Importing the OS Module
from cryptography.fernet import Fernet #Importing the Fernet Cryptography module

path = 'login.ini'  #Setting the path to 'login.ini' in the root directory of where the program is run
doesExist = os.path.exists(path) #Do the path exist?
cryptKey = b'0izq4WQA0SUbd-iyNI1SX1zoz6jNLh3aD7KWz6VlkVc=' #Setting the key to use during encryption/decryption
f = Fernet(cryptKey) #Creating the 'f' object to use functions on | Sets unique instance of Fernet class to use across the progrum

if not doesExist:                                               #If it don't exist
    userName = input('Username: ')                              #Take username input from use
    encryptedUsername = f.encrypt(userName.encode('utf-8'))     #Encrypt the user input for username
    userPass = input('Password: ')                              #Take password input from use
    encryptedPassword = f.encrypt(userPass.encode('utf-8'))     #Encrypt the user input for the password
    with open('login.ini', 'wb') as loginInfo:                  #If 'login.ini' doesn't exist, we're creating it and writing to it using bytes
        loginInfo.write(encryptedUsername)                      #Write the encrypted username on the first line
        loginInfo.write(b"\n")                                  #Breaking a line
        loginInfo.write(encryptedPassword)                      #Write the enctypted password on the second line
    loginInfo.close()                                           #Close the file we're messing with, common couretesy
else:                                                           #ELSE, IF EXIST
    with open('login.ini', 'r') as loginInfo:                   #We're gonna open 'login.ini' like ya moms legs
        accountInfo = []                                        #Set the accountInfo list to none
        for lines in loginInfo:                                 #Loop through the lines in the list
            if '\n' in lines:                                   #Checking the lines for newline indicators
                lines = lines.replace('\n', '')                 #Replacing the new line indicators
            accountInfo.append(lines.encode('utf-8'))           #Appending the new information to the accountInfo list

    user = f.decrypt(accountInfo[0])                            #Decrypting the username, index 0 of accountInfo
    password = f.decrypt(accountInfo[1])                        #Decrypting the password, index 1 of accountInfo

    #Decoding the byte object | Produces string object we can read/manipulate easily
    user = user.decode('utf-8')
    password = password.decode('utf-8')