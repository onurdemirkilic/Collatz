'''
GITHUB : https://www.github.com/onurdemirkilic
'''
print("\n")
print("\n")
print("GITHUB : https://www.github.com/onurdemirkilic")
print("\n")
print("\n")

while True : 
    try : 
        number = int(input("Enter a INTEGER input : ")) #our value
        if number == 0 : 
            print("Do not enter zero (0)") #Program doesnt allow 0
            continue
    except : 
        check_exit = input("Do you want to exit ? [Y/N]") #enter "y" to exit
        if check_exit.lower() == "y" : 
            exit()
        else : 
            continue

    if isinstance(number,int) == True : #checking number for integer value or not
        first_number = number
        order = 0
        while True : 
            if number == 1 : 
                break 
            if (number % 2) == 0 : #If a number is divisible by two 
                number = number / 2
                order += 1
                print(number)
            else : 
                number = ((number * 3 ) + 1)
                order += 1 
                print(number)

        print("Tried '{}' in '{}' time(s)".format(first_number,order)) #Entered input and total loop time
    else : 
        print("Your input is not ok,program is shutting down...")
        continue
