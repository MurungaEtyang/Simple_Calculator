class Calculation:
    __option = ""

    def __init__(self, options):
        self.__option == options

    def __calculation__(self):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if self.__option == "1":
            return f"Addition of {number1} and {number2} is {number1 + number2}"
        elif self.__option == "2":
            return f"Subtraction of {number1} and {number2} is {number1 - number2}"
        elif self.__option == "3":
            return f"Multiplication of {number1} and {number2} is {number1 * number2}"
        elif self.__option == "4":
            return f"Division of {number1} and {number2} is {number1 / number2}"


