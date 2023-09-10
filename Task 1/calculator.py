
def addition(num1,num2):
    """
    Adds two numbers together and returns the result.

    Parameters:
        num1 (int): The first number to be added.
        num2 (int): The second number to be added.

    Returns:
        int: The sum of num1 and num2.
    """
    return num1+num2

def subtraction(num1,num2):
    """
    Subtracts `num2` from `num1`.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The result of subtracting `num2` from `num1`.
    """
    return num1-num2

def multiplication(num1,num2):
    """
    Multiplies two numbers and returns the result.
    
    Args:
        num1 (int): The first number to be multiplied.
        num2 (int): The second number to be multiplied.
        
    Returns:
        int: The product of num1 and num2.
    """
    return num1*num2

def division(num1,num2):
    """
    Calculates the division of two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of dividing num1 by num2.
    """
    return num1/num2

def main():
    """
    Main function to execute the program.

    This function prompts the user to select an operation and two numbers for calculation.
    It then performs the selected operation on the two numbers and displays the result.

    Parameters:
        None

    Returns:
        None
    """
    while (True):
        
        print("Select operation.")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice = input("Enter choice(1/2/3/4):")
        if choice == '5':
            break
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        if (choice == '1'):
            print(num1,"+",num2,"=",addition(num1,num2))
        elif (choice == '2'):
            print(num1,"-",num2,"=",subtraction(num1,num2))
        elif (choice == '3'):
            print(num1,"*",num2,"=",multiplication(num1,num2))
        elif (choice == '4'):
            print(num1,"/",num2,"=",division(num1,num2))
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
