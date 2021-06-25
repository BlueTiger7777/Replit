def valinput():

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        try:
            X = int(input("Value:" ))
            Out = X

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        else:
            powerinput(X, Out)

def powerinput(X, Out):

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        try:
            Power = int(input("To The Power Of:" ))
            Power -= 1

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        else:
            calculate(X, Power, Out)

def calculate(X, Power, Out):
    while Power > 0:
        Out = Out*X
        Power -=1

    print("Answers =", Out)
    input("Press Enter To Calculate A New Power")
    valinput()

valinput()
