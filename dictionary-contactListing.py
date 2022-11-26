#Menu
        
print("<==========> Menu <==========> \n\n 1 -> Add item \n 2 -> Search \n 3 -> Exit (y/n) \n")
print("<============================>")

userList = {}

while True:
    #user input
    try:
        user_input = int(input("\nWhat do you want to do?(1-3)?: "))
    except:
        print("Error Input")
        exit()
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

        userDetails = {'name': userName,
                  'gender':userGender,
                  'age':userAge,
                  'email':userEmail,
                  'address':userAddress,
                  'contact':userContact }
        
        #Using the initial dictionary we transfer the userDetails inside another dictionary 
        userList[userName] = userDetails
    
        
        
    #if Option 2 Search function
    elif user_input == 2:
        print("\n<Type the name you want to search> \n")
        search = input("Name: ")
        
        if search in userList:
            print("\n<========= User's Info ============>\n")
            print("Name: " + userList[search]['name'])
            print("Gender: " + userList[search]['gender'])
            print("Age: " + userList[search]['age'])
            print("Email: " + userList[search]['email'])
            print("Address: " + userList[search]['address'])
            print("Contact Numer: " + userList[search]['contact'])
        else:
            print("\nName not in Database!\n")    
    #if Option 3
    elif user_input == 3:
        inputOption3 = input("Are you sure you want to exit? (y/n): ")
        if inputOption3 == 'y':
            break
    