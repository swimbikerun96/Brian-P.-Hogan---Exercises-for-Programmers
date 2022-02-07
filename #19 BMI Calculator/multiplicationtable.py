multiplier_in = input('Please enter the multiplier: ')
multiplier = int(multiplier_in)
multiplicand_in = input('Please enter the multiplicand: ')
multiplicand = int(multiplicand_in)

for x in range(multiplier):
        for y in range(multiplicand):
            z = x * y
            print(z, end="\t")
        print() #creates the space after the loop
