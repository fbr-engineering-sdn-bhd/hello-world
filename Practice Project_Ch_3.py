def collatz(number):
    
    
    try:
        number // 2 == 1
    except ValueError:
        
            print('Invalid')
            
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

for numbers in range(1,100):
    
    print('User input: ')
    
    print(collatz('User input: ' + str(input())))
`
