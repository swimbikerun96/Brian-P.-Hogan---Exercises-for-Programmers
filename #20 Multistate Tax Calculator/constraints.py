try:
    amount = input('What is the order amount? ')
    a = float(amount)
    state = input('What state do you live in? ')
    if state.lower() == 'wisconsin' or state.lower() == 'wi':
        #Calculation for state tax
        st = a * .05
        county = input('Which Wisconsin county do you live in? ')
        if county.lower() == 'eau claire':
            #Calculation for county tax
            ct = a * .005
        elif county.lower() == 'dunn':
            #Calculation for county tax
            ct = a * .004
        else:
            ct = 0
        #Calculation for a total
        total = ct + st + a
        #Create a single output statement
        output = f'The state tax is {"${:,.2f}".format(st)}\nThe county tax is {"${:,.2f}".format(ct)}\nThe total is {"${:,.2f}".format(total)}' 
    elif state.lower() == 'illinois' or state.lower() == 'il':
        #Calculation for state tax
        st = a * .08
        #Calculation for a total
        total = a + st
        #Create a single output statement
        output = f'The state tax is {"${:,.2f}".format(st)}\nThe total is {"${:,.2f}".format(total)}'
    else:
        output = f'Congratulations for not being in Wisconsin or Illinois!\nNo tax! Your total is {"${:,.2f}".format(a)}'
      
    print(output)

except ValueError:
    print('Please ensure states are entered as text')
