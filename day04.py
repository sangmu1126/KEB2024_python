subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]
#print(subjects[::-1])
#subjects[::-1]
#subjects = subjects[::-1]  # subjects.reverse()
print(subjects)
#subjects.remove("Java")
#del subjects[-2]
#del subjects[2]
# subjects.pop(2)
#subjects.sort(reverse=True)  # desc
copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)

#8.10까지 과제

import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
# print(drinks_foods)
# print(drinks_foods.pop("고량주"))
# print(drinks_foods)

#del drinks_foods["위스키"]
#drinks_foods["사케"] = "광어회"
japan_drinks_foods = {"사케": "광어회", "위스키": "낙곱새"}
drinks_foods.update(japan_drinks_foods)

#drink = input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods)
# print(drinks_foods_keys)
# #print(drinks_foods_keys.pop(0))
# print(drinks_foods_keys.remove("위스키"))
# print(drinks_foods_keys)
#print(random.choice(drinks_foods_keys))

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다')
    elif menu == '6':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break
