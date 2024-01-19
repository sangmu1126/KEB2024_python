def test(func):
    def test_1():
        print('start')
        func()
        print('end')
    return test_1

def p():
    print('decorator')

p = test(p)
print(type(p))
print(p)

p()


