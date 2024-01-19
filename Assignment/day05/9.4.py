def OopsException():
    print('0으로 나눌 수 없어요')
n = list(map(int,input('두 개의 자연수 입력: ').split(' ')))
n[0], n[1] = max(n), min(n)
try:
    print(f'두 수를 나누면 {n[0]/n[1]}')
except:
    OopsException()
