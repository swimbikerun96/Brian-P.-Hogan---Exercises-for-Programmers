
words = []

while True:
    #prompt the user for the word and then add it to the empty list defined above
    string = input("Please input a word: ")
    words.append(string)

    if len(words)%5 == 0:
        calculate = input("Calculate number of characters? (Y/N) ")
        #Limits the user to entering 5 words entered at a time, providing a periodic check on the number of words to calculate

        if calculate.lower() == "y":
        #Ensures the user wants to calculate the number of characters and then provides a count for all words entered

            for word in words:
                count = len(word)
                print(f"There are {count} letters in the word '{word}'!")

            print("Program Exited")
            break

        elif calculate.lower() == "n":
            #Gives the user the option to either continue entering words or exit the program
            keep_going = input("Continue adding words to count? (Y/N) ")

            if keep_going == "n":
                print("Program Exited")
                break
            elif keep_going == "y":
                continue

        else:
            # if the user enters neither "y" nor "n", then this gives them the option to try again
            print("Please enter only 'Y' or 'N'")
            calculate = input("Calculate number of characters? (Y/N) ")

            if calculate.lower() == "y":

                for word in words:
                    count = len(word)
                    print(f"There are {count} letters in the word '{word}'!")
                print("Program Exited")
                break
            
            elif calculate.lower() == "n":
                keep_going = input("Continue adding words to count? (Y/N) ")
                if keep_going == "n":
                    print("Program Exited")
                    break
                elif keep_going == "y":
                    continue
        
        
    
