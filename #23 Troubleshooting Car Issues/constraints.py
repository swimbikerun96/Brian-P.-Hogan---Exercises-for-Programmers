#Silent car question
while True:
    sc = input('Is the car silent when you turn the key? ')
    if sc.lower() == 'yes' or sc.lower() == 'y':
        #Question for coroded battery terminals
        while True:
            cbt = input('Are the Battery terminals coroded? ')
            if cbt.lower() == 'yes' or cbt.lower() == 'y':
                print('Clean terminals and try starting again.')
                break
            elif cbt.lower() == 'no' or cbt.lower() == 'n':
                print('Replace cables and try again.')
                break
            else:
                print('Only "Yes" or "No" are acceptable answers.')
                continue
    elif sc.lower() == 'no' or sc.lower() == 'n':
        #Question for clicking noise
        while True:
            cn = input('Does the car make a clicking noise? ')
            if cn.lower() == 'yes' or cn.lower() == 'y':
                print('Replace the battery.')
                break
            elif cn.lower() == 'no' or cn.lower() == 'n':
                #Question for engine cranking up
                while True:
                    cu = input('Does the car crank up but fail to start?')
                    if cu.lower() == 'yes' or cu.lower() == 'y':
                        print('Check the spark plug connections.')
                        break
                    elif cu.lower() == 'no' or cu.lower == 'n':
                        #Question for engine starting then dying
                        while True:
                            stn = input('Does the engine start and then die? ')
                            if stn.lower() == 'yes' or stn.lower() == 'y':
                                #Question for Fuel Injection
                                while True:
                                    fi = input('Does your car have fuel injection? ')
                                    if fi.lower() == 'yes' or fi.lower() == 'y':
                                        print('Get it in for service')
                                        break
                                    elif fi.lower() == 'no' or fi.lower() == 'n':
                                        print('Check to ensure the choke is opening and closing.')
                                        break
                                    else:
                                        print('Only "Yes" or "No" are acceptable answers')
                                        continue
            else:
                print('Only "Yes" or "No" are acceptale answers.')
                continue
    else:
        print('Only "Yes" or "No" are acceptale answers.')
        continue
