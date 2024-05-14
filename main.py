from Calculation import Calculation
class MainWindow():
    def __init__(self):
        pass

    def calculator(self):
        print("Choose option \n")
        print(["1. start a calculator", "0. Close the program"])

        while True:
            start = input("select option: ")

            if start == '1':
                while True:
                    print(["1. Add", "2. Sub", "3. Mul", "4. Div"])
                    maths_calculation = input("Select option: ")
                    cal = Calculation(maths_calculation)
                    if maths_calculation == "1":
                        cal.__calculation__()
                    elif maths_calculation == "2":
                        cal.__calculation__()
                    elif maths_calculation == "3":
                        cal.__calculation__()
                    elif maths_calculation == "4":
                        cal.__calculation__()
                    else:
                        print("Wrong choice")
            elif start == '0':
                break
            else:
                print("Wrong option")


if __name__ == "__main__":
    my_class = MainWindow()
    print(my_class.calculator())
