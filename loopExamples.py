# testing If loops, condition, while loops and for loops


def loopExamples():

    i = 1

    if i == 1:
        print("Successful")

    elif i != 1:
        print("Unsuccessful")
        return loopExamples()

    while i <= 5:
        print("Hey ,this is a while loop, please break it! ")
        break


def moreLoopExamples():

    sampleArray = ["Foo", "Bar"]

    for x in sampleArray:
        print(sampleArray[0])
        break

    # Input controlled logic
    userInput = int(input("Write a number: "))
    numArray = []
    # Let's assume we want to take userinput for a number, so we can append it to the array, then do a for loop using the same array.
    for y in range(0, userInput):
        # moreNums = float(input()) # Assume the user wants to input decimal number, we could then switch this up using float(input()) to get the same result.
        numArray.append(userInput)
        print(numArray)
        break

    # Now let's test If and while loops using numbers, while concatinating strings to make a simple dynamic little program.


def ifStatements():
    moreUserInput = int(input("Write yet another number: "))
    # I try to not use more than a maximum of 1 or 2 elif statements, considering there are better options, Python however does not have a switch statement.
    if moreUserInput <= 5:
        print("Your number is ", moreUserInput, "or less")
    elif moreUserInput <= 500:
        print("Your number is ", moreUserInput, "or less")
    # This is a very big number, but we could mathematically envision that this number or rather integer is infitnite as long as it is a whole number, so I max it at 5 million as that is probably high enough.
    elif moreUserInput <= 5000000:
        print("Your number is", moreUserInput, "")
    # The else ends the logical conditions and moves the program forward so to say.
    else:
        print("Exiting...")
        exit()
