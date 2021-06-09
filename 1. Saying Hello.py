

while True:
    #Use a While Loop to continuously prompt the user for input
    name = input("Please enter your name: ")
    name_list = list(name.lower())
    vowel_list = ["a","e","i","o","u"]

    if name_list[0] in vowel_list:
        #This if statement checks to see if the input name begins with a vowel
        concatenation = "Your name begins with a vowel! A pleasure, " + name
        print(concatenation)
        #Separate the concatenation from the output statement
        again = input("Once more? ")
        #prompts the user to continue
        
        if again.lower() == "n":
            #checks to see if the user is finished
            print("Program Exited.")
            break
        elif again.lower() == "y":
            #checks to see if the user would like to input another name
            continue
        else:
            #Handles the input if it is neither 'y' not 'n'
            another = input("Please enter either 'N' or 'Y': ")
            if another.lower() == "y":
                continue
            elif another.lower() == "n":
                print("Program Done")
                break

    else:
        concatenation = "Nice to meet you, " + name + "!"
        print(concatenation)
        #Separate the concatenation from the output statement

        again = input("Once more? ")
        #prompts the user to continue
        
        if again.lower() == "n":
            #checks to see if the user is finished
            print("Program Exited.")
            break
        elif again.lower() == "y":
            #checks to see if the user would like to input another name
            continue
        else:
            #Handles the input if it is neither 'y' not 'n'
            another = input("Please enter either 'N' or 'Y': ")
            if another.lower() == "y":
                continue
            elif another.lower() == "n":
                print("Program Done")
                break
        
            



        
