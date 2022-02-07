#State Tax Dictionary
states = {
    'pennsylvania': .06,
    'pa': .06,
    'wisconsin': .05,
    'wi': .05,
    'illinois': .08,
    'il': .08
    }
#Wisconsin Counties
wc = {
    'eau claire': .005,
    'dunn': .004
    }

#Pennsylvania counties
pc = {
    'allegheny': .01
    }

#Inputs
amount = input('What is the order amount? ')
a = float(amount)
state = input('What state do you live in? ')
county = input('What county do you live in? ')

#Initial check for state tax
try:
    st = states[state]
except KeyError:
    st = 0
    
#Check for county tax
try:
    if state.lower() == 'wi' or state.lower() == 'wisconsin':
        ct = wc[county]        
    elif state.lower() == 'pa' or state.lower() == 'pennsylvania':
        ct = pc[county]
    else:
        ct = 0
except KeyError:
    ct = 0

#county Tax Final
ctf = "${:,.2f}".format(ct * a)
#state tax final
stf = "${:,.2f}".format(st * a)
#Total final
tf = "${:,.2f}".format((st*a)+(ct*a)+a)

if st > 0:
    output = f'The Sales Tax is {stf}\nThe County Tax is {ctf}\nThe total is {tf}'
else:
    output = f'The total is {tf}'

print(output)

    


