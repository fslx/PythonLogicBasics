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

    sampleArray = ["Foo", "Bar", ]

    for x in sampleArray:
        print(sampleArray[0])
        break

    # Input controlled logic
    userInput = input("Write something cool here: ")
    sampleArray.append(userInput)
    # Let's assume we want to take userinput for a string, so we can append it to the array, then do a for loop using the same array.
    for x in sampleArray:
        print(sampleArray[2])
        break

    # Now let's test If and while loops using numbers, while concatinating strings to make a simple dynamic little program.

    moreUserInput = float(input)

    if moreUserInput <= 5:
        print("Your number is either " + moreUserInput + " " + "or less")
    elif moreUserInput <= 500:
        print("Your number is either " + moreUserInput + " " + "or lower")
