#Menu
print("<==========> Menu <==========> \n\n 1 -> Add item \n 2 -> Search \n 3 -> Exit (y/n) \n")
print("<============================>")

#user input
user_input = int(input("\nWhat do you want to do?(1-3)?: "))


#if Option 1
if user_input == 1:
    userList = {}
    
    #User Info with user input
    print("\n<==========>Fill up the given information<==========>\n")
    userName = input("Full Name: ")
    userAge = input("Age: ")
    userEmail = input("Email: ")
    userAddress = input("Address: ")
    userPhone = input("Phone Number: ")
    print("\nThe user is now in the directory.\n")
    
    user = {
        userName : {
            "name" : userName,
            "age" : userAge,
            "email" : userEmail,
            "address" : userAddress,
            "phone" : userPhone 
        }
    } 
    
    print(user)
    
#if Option 2
#if Option 3