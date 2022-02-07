#Function for Fahrenheit To Celsius
def ftc(degrees):
    f = degrees
    c = (f-32) * (5/9)
    return f'The temperature in Celsius is {c}'
#Function for Farhenheit to Kelvin
def ftk(degrees):
    f = degrees
    k = (((f - 32) * 5)/9) + 273.15
    return f'The temerature in Kelvin is {k}'
#Function for Celsius To Fahrenheit
def ctf(degrees):
    c = degrees
    f = ((c*9)/5) + 32
    return f'The temperature in Fahrenheit is {f}'
#Function for Celsius to Kelvin
def ctk(degrees):
    c = degrees
    k = c + 273.15
    return f'The Temperature in Kelvin is {k}'
#Function for Kelvin to Fahrenheit
def ktf(degrees):
    k = degrees
    f = (((k-273.15)*9)/5) + 32
    return f'The Temperature in Fahrenheit is {round(f,2)}'
#Function for Kelvin to Celsius
def ktc(degrees):
    k = degrees
    c = k - 273.15
    return f'The Temperature in Celsius is {round(c,2)}'
while True:
    try:
        #variable to capture temperature scale
        ts = input('Press C to input Celsius.\nPress F to input Fahrenheit.\nPress K to input Kelvin.')
        if ts.lower() == 'f' or ts.lower() == 'c' or ts.lower() == 'k':
            print(f'Your choice: {ts.upper()}')
            break
        else:
            raise ValueError
    except ValueError:
        print('Only "C", "F", or "K" Please!')
        continue

while True:
    try:
        if ts.lower() == 'f':
            #variable for temperature in
            ti = input('Please Enter the Temperature in Fahrenheit: ')
            degrees = float(ti)
            output1 = ftc(degrees)
            output2 = ftk(degrees)
            break
        elif ts.lower() == 'c':
            ti = input('Please Enter the Temperature in Celsius: ')
            degrees = float(ti)
            output1 = ctf(degrees)
            output2 = ctk(degrees)
            break
        elif ts.lower() == 'k':
            ti = input('Please Enter the Temperature in Kelvin: ')
            degrees = float(ti)
            output1 = ktf(degrees)
            output2 = ktc(degrees)
            break
    except ValueError:
        print('Numerical Values Only!')
        continue

print(output1)
print(output2)
