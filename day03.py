# prime number
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

<<<<<<< HEAD
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
=======
for number in range(n1, n2+1):
    is_prime = True
>>>>>>> 5a76e5d14ff24a7028ef7a3c40655cdb7c40db06

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
