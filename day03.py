# prime number
number = int(input("Input number : "))
is_prime = True

subjects = {'python':'kim', 'c++':'sung', 'database':'kang', 'linux':'lee'}
print("{0[python]} {0[c++]}".format(subjects))

if number < 2:
    print(f'{number} is NOT prime number!')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i = i + 1

    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number!')
