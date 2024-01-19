#generator
def get_odds():
    for i in range(10):
        if i%2==1:
            yield i
r = get_odds()

cnt = 1
for k in r:
    if cnt==3:
        print(k)
    cnt+=1
