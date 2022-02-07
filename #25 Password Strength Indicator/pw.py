#Create lists to check the password entered against
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = [' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\'',']','^','_','`','{','|','}','~']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def passwordValidator(password):
    #Create a list to store password characters in
    mylist = []
    #Check for Weak and Very Weak Passwords
    if len(password) == 0:
        return 0
    elif len(password) < 8:
        if password.isnumeric() == True:
            return 1
        elif password.isalpha() == True:
            return 2
        else:
            return 3
    #Check for Strong and Very Strong Passwords
    elif len(password) >= 8:
        for character in password:
            if character.isdigit() == True:
                mylist.append("Numbers")
            elif character.isalpha() == True:
                mylist.append("Letters")
            elif character in special_characters:
                mylist.append("sc")
        if "sc" in mylist and "Letters" in mylist and "Numbers" in mylist:
            return 5
        elif "Letters" in mylist and "Numbers" in mylist:
            return 4
        else:
            return 6
        
            




