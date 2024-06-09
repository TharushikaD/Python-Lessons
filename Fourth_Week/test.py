# fruits = ['apple', 'pear', 'orange']

# fruits[1]='banana'

# print(fruits)

# fruits.append("banana")

# print(fruits)

# number = (1,2,3,4,5,6,6)
# print(set(number))

# .count() method is used to count the number of non-overlapping occurrences of a substring in the string. 
# str = "Hello Little One"

# # print(str.count('l'))

# count=0

# for item in str:
#     if item=="l":
#         count +=1
        
# print(f"l count is {count}")

# print(str.upper())

# ------------------------

# username = "tom"
# password = "123"

# username1 = input("Enter your username: ")
# password1 = input("Enter your password: ")
    
# if (username1.lower().strip()== username) and (password1 == password):
#     print("Login Successful")
# else:
    
#     print("Incorrect username or Password")

# ------------------------

# numbers = [1,4,8,12,16]

# Explanation: Starts from the last element and selects every second element moving backwards.
# print(numbers[-1::-2])
# Explanation: Starts from the third-to-last element and includes all elements to the end.
# print(numbers[-3:])

# ------------------------

# val=input("Enter True of False: ")

# def chang_mode (val:str)->bool:
#     var =None
#     if val=="True":
#         var = False
    
#     if val == "Fales":
#         var = True
        
#     return var
    
# print(chang_mode(val))    
    
# ------------------------



# startno=int(input("Enter the Starting Number : "))
# endno=int(input("Enter the Ending Number : "))
# number_list = [n for n in range(startno,endno,1)]
# print("number_list ", number_list)

# # even_no =[num for num in list1 if num % ==0]

# # print(even_no)

# def checked_odd_or_even(numbers:list)-> dict:
#     odd_list = []
#     even_list = []
    
#     for number in numbers:
#         if int(number)%2==0:
#             even_list.append(number)
         
#         else:
#          odd_list.append(number)
         
#     return {
#         "odd_list":odd_list,
#         "even_list":even_list
#     }
    
# print(checked_odd_or_even(number_list))
    
    


    


 
