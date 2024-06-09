# email = input("Please enter your email address: ")

# def check_validity_email(email:str)->bool:
#     """"this function check the valifity of the email that you enter"""  
#     if email.count('@') ==1:
#         split_email = email.split('@')
#         if len(split_email[0]) > 2 and len(split_email[1]) > 2:
#             return True
#     else:
#         return False   

# print(f"Your Email is {check_validity_email(email)}")

from emailvalidation import Validation

email=input("Please enter the email: ")

print(f"Your Email is {Validation.check_validity_email(email)}")