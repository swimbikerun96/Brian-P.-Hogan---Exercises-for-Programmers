#Dictionaries to Replace Variables
dictionary1 = {
    "name" : "name"
    }
dictionary2 = {
    "output" : "output"
    }

#Input
dictionary1["name"] = input('What is your name? ')

#String Concatenation
if len(dictionary1["name"]) >= 5:
    dictionary2["output"] = f'Salutations, {dictionary1["name"]}!'
else:
    dictionary2["output"] = f'Hello, {dictionary1["name"]}, nice to meet you!'
    
#Output
print(dictionary2["output"])
