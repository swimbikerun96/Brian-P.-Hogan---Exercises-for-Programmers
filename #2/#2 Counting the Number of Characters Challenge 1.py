#Handle Input
while True:
    string_in = input("What is the input string? ")
    count = len(string_in)
    if count == 0 or string_in.isspace() == True:
        print('Please enter a string to continue')
        continue
    else:
        break

#Concatenate output
if count == 1:
    output = f'{string_in} is {count} character'
else:
    output = f'{string_in} has {count} characters'

#Display output
print(output)

