guess_me = 5
for number in range(10):
    if (guess_me > number):
        print("too low")
    elif (guess_me == number):
        print("found it!")
        break
    else:
        print("oops")
        break