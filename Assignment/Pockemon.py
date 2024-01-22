import random

class Pockemon:
    def __init__(self, name):
        self.name = name
        #self.type = type
        #hp
    def attack(self,attType,defType):
        pass
    def setSkill(self, skillList):
        self.skills = skillList
    def getSkills(self):
        return self.skills


    #def attack(self):
    def info(self):
        print(f'이름 : {self.name}')
        print(f'레벨 : {self.level}')
        print(f'타입 : {self.type}')
        print(f'기술 : {self.skill}')

class Level(Pockemon):
    def __init__(self, name, lev):
        super().__init__(name)
        self.level = lev
    def setLevel(self, num, name):
        self.level = PockemonList[self.name]
    def getLevel(self, Level):
        print()
    def levelUp(self):
        self.level += 1

class Type(Pockemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
class MyMon(Pockemon):
    def __init__(self, name, level=1):
        super().__init__(name)
        self.level = level

    # def evolve(self):
    #     if (self.name)
    #     elif
    #     print(f"{Character.name}은(는) {name}으로 진화했다!")
    def store(self):
        print(f"{self.name}은 완전히 회복되었다!")
    def rivalMon(self):
        if self.name == '이상해씨':
            rivalPkm = '리자몽'
        elif self.name == '파이리':
            rivalPkm = '거북왕'
        elif self.name == '꼬부기':
            rivalPkm = '이상해꽃'
        else:
            rivalPkm = '이브이'

class EnemyMon(Pockemon):
    def __init__(self, name):
        super().__init__(name)
class WildMon(Pockemon, Level):
    def __init__(self, name):
        super().__init__(name)
    def begin_(self):
        print(f"야생의 {self.name}이/가 나타났다!")

# class Skills:
#     def __init__(self):

class Character:
    def __init__(self, name):
        self.name = name

    def move(self, loc, idx):
        print()
        return loc[idx+1]
    def run(self, enemy):
        print(f"{self.name}은 {enemy.name}으로부터 간신히 도망쳤다..!")
    def watchDict(self):
        print(f'{Character.name}은 도감을 본다.')
    def dead(self):
        quit()

PockemonType = ['노말', '불', '물', '풀', '전기', '얼음', '격투', '독', '땅', '비행', '에스퍼', '벌레', '바위',
                '고스트', '드래곤', '악', '강철']
PockemonStarting = ['이상해씨', '파이리', '꼬부기', '피카츄']
PockemonEv1 = ['이상해풀', '리자드', '어니부기']
PockemonEv2 = ['이상해꽃', '리자몽', '거북왕']
PockemonLev1 = {'캐터피' : 2, '구구':3, '뿔충이':4, '꼬렛':2}
PockemonLev2 = {'니드런' : 8, '모래두지':11, '아보':13, '깨비참' : 9}
PockemonLev3 = {'파라스' : 13, '골뱃' : 17, '고라파덕' : 14, '우츠동' : 15}
PockemonLev4 = {'찌리리공':20,'텅구리':25,'시드라':29, '폴리곤':28}
PockemonLev5 = {'레어코일':30, '롱스톤':31, '날쌩마':38,'아쿠스타':36}
PockemonLev6 = {'강챙이':42,'시라소몬':45, '홍수몬':45, '또도가스':48}
PockemonLev7 = {'마그마':50, '에레브':50, '쁘사이저':54,'팬텀':52,'투구푸스':57}
PockemonLev8 = {'프테라' : 60, '괴력몬':62,'후딘':63,'코뿌리' : 68, '나인테일': 64}
PockemonLev9 = {'라프라스': 84, '갸라도스' : 88, '켄타우로스' : 81, '망나뇽' : 91}
PockemonLev10 = {'프리져' : 74, '썬더' : 75, '파이어' : 76}
PockemonFinal = {'뮤츠': 100}
PockemonChampion = {'역상성' : 92, '나시' : 81, '갸랴도스' : 84, '후딘' : 85, '마기라스' : 88, '윈디' : 90 }
PockemonRed = {'피카츄' : 100, '잠만보' : 96, '라프라스': 94, '이상해꽃' : 97, '거북왕': 98, '리자몽' : 99}
PockemonList = [PockemonLev1,
                PockemonLev2,
                PockemonLev3,
                PockemonLev4,
                PockemonLev5,
                PockemonLev6,
                PockemonLev7,
                PockemonLev8,
                PockemonLev9,
                PockemonLev10,
                PockemonChampion,
                PockemonFinal,
                PockemonRed]

# PockemonType = ['노말', '불', '물', '풀', '전기', '얼음', '격투', '독', '땅', '비행', '에스퍼', '벌레', '바위',
#                 '고스트', '드래곤', '악', '강철',
#                 ]
normal_skill = ['몸통박치기', '속이다', '신속', '이판사판태클', '파괴광선']
fire_skill = ['화염자동차', '화염방사', '플레어드라이브', '불대문자', '오버히트']
water_skill = ['물대포', '아쿠아테일', '파도타기', '하이드로펌프', '하이드로캐논']
glass_skill = ['잎날가르기', '리프블레이드', '우드해머', '솔라빔', '리프스톰']
electric_skill = ['전자기파', '와일드볼트', '십만볼트', '전자포', '번개']
ice_skill = ['얼음뭉치', '얼다바람', '냉동빔', '눈보라', '프리즈드라이']
fighting_skill = ['마하펀치', '깨뜨리다', '파동탄', '무릎차기', '인파이트']
poison_skill = ['독찌르기', '베놈쇼크', '오물웨이브', '맹독', '더스트슈트']
flying_skill = ['날개치기', '공중날기', '브레이브버드', '불새', '폭풍']
psychic_skill = ['염동력', '사이코쇼크', '사념의박치기', '사이코키네시스', '꿈먹기']
ground_skill = ['진흙뿌리기', '구멍파기', '땅고르기', '대지의힘', '지진']
bug_skill = ['벌레먹음', '흡혈', '시저크로스', '벌레의야단법석', '메가폰']
rock_skill = ['암석봉인', '스톤샤워', '원시의힘', '스톤엣지', '양날박치기']
ghost_skill = ['야습', '괴상한바람', '섀도크루', '섀도볼', '고스트다이브']
dragon_skill = ['더블촙', '용의파동', '드래곤다이브', '역린', '용성군']
evil_skill = ['따라가때리기', '보복', '탁쳐서떨구기', '악의파동', '속임수']
stell_skill = ['불릿펀치', '메탈크로우', '아이언헤드', '러스터캐논', '코멧펀치']
mewtwo_skill = ['미래예지', '파동탄', 'HP회복', '사이코커터', '사이코브레이크']

skills = [normal_skill, fire_skill, water_skill, glass_skill,electric_skill,ice_skill,fighting_skill,poison_skill,
flying_skill,psychic_skill,ground_skill,bug_skill,rock_skill,ghost_skill,dragon_skill,evil_skill,stell_skill,mewtwo_skill]

damage = dict()
for sk in skills:
    for i, skill in enumerate(sk):
        damage[skill] = i+1

skill_type = dict(zip(PockemonType, skills))
print(skill_type)
print(damage)

locations = ['태초마을', '1번도로', '상록시티', '회색시티', '블루시티', '보라타운',
             '홍련마을', '석영고원', '23번도로', '포켓몬리그', '이름없는동굴', '28번도로','은빛산']
def checkPkmName(pkm):
    if (pkm in PockemonStarting):
        return pkm
    elif pkm.isdigit():
        if (int(pkm)-1) >= 0 and (int(pkm)-1) < len(PockemonStarting):
            return PockemonStarting[int(pkm)-1]
    else:
        return False
def findPkm(num):
    if num == 1:
        return
# PkmType()

# GAME START
print("포켓몬스터 PYTHON")
print("""
    포켓몬 세계에 온 것을 환영한다!
    나는 포켓몬을 연구하는 오박사 라고 한다.
""")
chrName = input('너의 이름은 무엇이니? : ')
Chr = Character(chrName)
print(f"""
    반갑구나, {Chr.name}.
    이 세계에는 수많은 포켓몬들이 있단다.
    이곳을 여행하기 위해서는 포켓몬의 도움이 필요해.   
    """)
startPkm = input('너와 함께할 포켓몬을 고르렴!\n'
                 '1. 이상해씨\n'
                 '2. 파이리\n'
                 '3. 꼬부기\n'
                 '4. 피카츄\n\n'
                 '당신의 포켓몬은? : ')

if (checkPkmName(startPkm)):
    myPkm = MyMon(checkPkmName(startPkm))
else:
    print("""
        그 포켓몬은 고를 수 없어...
        너는 이곳과 맞지 않는 것 같구나...    
    """)
    quit()

print(f"""
    좋아, 이제부터 너의 포켓몬은 {myPkm.name}다!
    세계를 여행하고 성장하며 포켓몬 마스터가 되기위해 노력하렴.
    내가 지켜보고 있으마. 또 보자꾸나!
    """)
print("="*150)
loc = locations[0]
print("\n현재 위치 : 태초마을\n")

act = 0
while True:
    act = int(input('무엇을 할까?\n'
                    '1) 포켓몬과 배틀\n'
                    '2) 다음 마을로 이동\n'
                    '3) 내 포켓몬의 정보\n'
                    '4) 도감을 확인한다\n'
                    '5) 현재 위치 확인\n'
                    '0) 종료\n'
                    '숫자를 입력하세요 : '
                    ))
    if act==1:
        print('')
        print("="*150)
        loc = Chr.move(locations, 0)
        print(f"현재 위치 : {loc}")
        nowWild = WildMon(random.choice([i for i in PockemonLev1]))
        nowWild.level(PockemonLev1[nowWild.name])
        print(f"""
    야생의 {nowWild.name} (nowWild.level) 이/가 나타났다!
    가라 {myPkm.name}!
        """)
        toDo = input('무엇을 할까?\n'
                         '1. 전투\n'
                         '2. 도망친다\n'
                         '숫자를 입력하세요 : ')
        if toDo==1:
            print()
        else:
            pass
        if toDo==1:
            print('skills')
        else:
            print("""   무사히 도망쳤다...!""")
            print("""   상대 레벨이 높아 도망칠 수 없다!""")
    elif act==2:
        pass
    elif act==3:
        pass
    elif act==4:
        pass
    elif act==0:
        real = input('정말로 모험을 그만둘꺼니? (y/n) : ')
        if real=='y':
            break
            quit()

    print()