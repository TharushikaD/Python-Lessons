import re

# Class Definition:
class Validation:
    
# This defines a method named check_validity_email inside the Validation class.
# It takes one parameter, email, which is expected to be a string (str).
# The method is supposed to return a boolean value (bool), which means it will return either True or False.
# This line defines a regular expression (regex) pattern stored in the variable regex.
# This checks if the email string matches the regex pattern using re.match().s
    def check_validity_email(email:str)-> bool:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'   
        if re.match(regex, email):
            return True
        else:
            return False