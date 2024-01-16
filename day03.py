#subjects = {'python':'kim', 'c++':'sung', 'database':'kang', 'linux':'lee'}
#print("{0[python]} {0[c++]}".format(subjects))

# prime number
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        #pass
        continue
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
