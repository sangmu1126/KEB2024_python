def test(func):
    def test_1():
        print('start')
        func()
        print('end')
    return test_1

@test
def p():
    print('decorator')

p()


