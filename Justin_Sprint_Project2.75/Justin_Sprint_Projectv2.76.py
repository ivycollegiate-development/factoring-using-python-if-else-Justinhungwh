List all of factors of a values
def list_factors(n):
    # Explain the line of code belowg
    return [i for i in range (1, n+1) if n % i == 0]
    # This will take whatever number we put in and check for factors using a list

    _name_=='__main__':# Checks to see if the application is running locally
    #Ask the user for a number
    user_input = input('Please enter a number here')
    # Convert that user to an interger
    number = int(user_input)
    # Check to see if the u=number is positive or negative
    if number <= 0:
        print('Please enter a positive number. ')
        else:
            # Get the factors for that value input
            factors = list_factors(number)
            # Print the facors of the input value 
            print(f'The factors of {number} are {factors}')

except ValueError:

Handles the exception negative values or 0
print That is an invalid number. Please a positive interger.')