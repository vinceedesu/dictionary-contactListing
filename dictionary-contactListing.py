#Menu
        
print("<==========> Menu <==========> \n\n 1 -> Add item \n 2 -> Search \n 3 -> Exit (y/n) \n")
print("<============================>")

while True:
    #user input
    user_input = int(input("\nWhat do you want to do?(1-3)?: "))


    #if Option 1
    if user_input == 1:
        
        #User Info with user input
        print("\n<==========>Fill up the given information<==========>\n")
        userName = input("Full Name: ")
        userGender = input("Gender: ")
        userAge = input("Age: ")    
        userEmail = input("Email: ")
        userAddress = input("Address: ")
        userContact = input("Contact Number: ")


#My Reference https://www.geeksforgeeks.org/python-nested-dictionary/

    Dict = {
        userName:{'name': userName,
                  'gender':userGender,
                  'age':userGender,
                  'age':userAge,
                  'email':userEmail,
                  'address':userAddress,
                  'contact':userContact }
    }
    
    print("\nThe user is now in the directory.\n")
    print("The user information has been saved!\n")
        
        
    #if Option 2
    
    #if Option 3