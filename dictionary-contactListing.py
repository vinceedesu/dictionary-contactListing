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
        print("\nThe user is now in the directory.\n")
        print("The user information has been saved!\n")

#My Reference https://www.geeksforgeeks.org/python-nested-dictionary/

    userDetails = {
        userName:{'name': userName,
                  'gender':userGender,
                  'age':userAge,
                  'email':userEmail,
                  'address':userAddress,
                  'contact':userContact }
    }
    
        
        
    #if Option 2 Search function
    if user_input == 2:
        print("\n<Type the name you want to search> \n")
        search = input("Name: ")
        
        print("\n<========= User's Info ============>\n")
        print("Name: " + userDetails[search]['name'])
        print("Gender: " + userDetails[search]['gender'])
        print("Age: " + userDetails[search]['age'])
        print("Email: " + userDetails[search]['email'])
        print("Address: " + userDetails[search]['address'])
        print("Contact Numer: " + userDetails[search]['contact'])
        
    #if Option 3
    
    if user_input == 3:
        inputOption3 = input("Are you sure you want to exit? (y/n): ")
        if inputOption3 == 'y':
            break