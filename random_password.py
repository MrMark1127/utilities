# Importing random to generate
# random string sequence
import random
  
# Importing string library function
import string

special_characters = "!@#$%^&*()"

def rand_pass(size):
    
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(
                        string.ascii_letters + string.digits + special_characters)
                        for n in range(size)])
    
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecialCharacter = False

    for a in generate_pass:
        if (a.isupper()) == True:
            hasUpper = True
        if (a.islower()) == True:
            hasLower = True
        if (a.isdigit()) == True:
            hasDigit = True
        if a in special_characters:
            hasSpecialCharacter = True
        
    if hasUpper and hasLower and hasDigit and hasSpecialCharacter:
        return generate_pass

password = rand_pass(16)
print(password)