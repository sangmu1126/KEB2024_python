import random

# Classes
class Pockemon:
    def __init__(self, name):
        self.name = name

    def hpCon(self, damage):
        self.hp -= damage
        print(f"""
    {self.name} 는(은) {damage}의 피해를 입었다!""")
        if (self.hp <= 0):
            global isOver
            isOver = True
            print(f"""
    {self.name} 는(은) 쓰려졌다!""")
    # def setLv(self, pkmList):
    #     self.level = pkmList[self.name][0]
    def setInfo(self, pkmList):
        self.level = pkmList[0]
        self.type = pkmList[1]
        self.hp = 10 + 490 * (self.level-1)/99
    def getLevel(self):
        return self.level

    def getType(self):
        return self.type

    def attack(self,attType,defType):
        pass
    # def setSkill(self, skillList):
    #     self.skills = skillList
    def getSkills(self, type):
        return skill_type[type]

    #def attack(self):
    def getInfo(self):
        print(f'이름 : {self.name}')
        print(f'레벨 : {self.level}')
        print(f'타입 : {self.type}')
        print(f'기술 : {self.skill}')

    def lvUp(self):
        self.level += 1

# class Level(Pockemon):
#     def __init__(self, name, lev):
#         super().__init__(name)
#         self.level = lev
#     def setLevel(self, num, name):
#         self.level = PockemonList[self.name]
#     def getLevel(self, Level):
#         print()
#     def levelUp(self):
#         self.level += 1

# class Type(Pockemon):
#     def __init__(self, name, type):
#         super().__init__(name)
#         self.type = type
#     def getType(self):
#         return self.type

# class Skill(Type, Pockemon):
#     def __init__(self, type, skills):
#         super().__init__(self, type)
#         self.skills = skills


class MyMon(Pockemon):
    def __init__(self, name):
        super().__init__(name)
    def myNum(self):
        if self.name=='이상해씨':
            return 0
        elif self.name=='파이리':
            return 1
        elif self.name=='꼬부기':
            return 2
        else:
            return 3
    # def evolve(self):
    #     if (self.name)
    #     elif
    #     print(f"{Character.name}은(는) {name}으로 진화했다!")
    def restore(self, pkmList):
        self.hp = 10 + 490 * (pkmList[0] - 1) / 99
        print(f"""
    {self.name} 는(은) 완전히 회복되었다!""")

    def rivalMon(self):
        if self.name == '이상해씨':
            rivalPkm = '리자몽'
        elif self.name == '파이리':
            rivalPkm = '거북왕'
        elif self.name == '꼬부기':
            rivalPkm = '이상해꽃'
        else:
            rivalPkm = '이브이'
    def win(self, isWin):
        if isWin==1:
            self.lvUp()
            return True

class EnemyMon(Pockemon):
    def __init__(self, name):
        super().__init__(name)
class WildMon(Pockemon):
    def __init__(self, name, lev):
        super().__init__(name, lev)
    def begin_(self):
        print(f"야생의 {self.name} 이/가 나타났다!")

# class Skills:
#     def __init__(self):

class Character:
    def __init__(self, name):
        self.name = name

    def move(self, loc):
        global locIdx
        locIdx += 1
        return loc[locIdx]
    def run(self, myLev, enemyLev):
        if myLev < enemyLev:
            print("""\n   상대 레벨이 높아 도망칠 수 없다!""")
        else:
            print("""\n   무사히 도망쳤다...!""")
    def watchDict(self):
        print(f'{Character.name} 는(은) 도감을 본다.')
    def dead(self):
        print(f"""
{self.name} 는(은) 눈 앞이 깜깜해졌다...
""")
        quit()

# Functions
def battleBegin():
    global isWin
    isWin = 0


def PkmChoice(locIdx):
    if locIdx == 1:
        return PockemonLev1
    elif locIdx == 3:
        return PockemonLev2
    elif locIdx == 5:
        return PockemonLev3
    elif locIdx == 7:
        return PockemonLev4
    elif locIdx == 9:
        return PockemonLev5
    elif locIdx == 11:
        return PockemonLev6
    elif locIdx == 13:
        return PockemonLev7
    elif locIdx == 15:
        return PockemonLev8
    elif locIdx == 17:
        return PockemonLev9
    elif locIdx == 19:
        return PockemonLev10
    else:
        return None
def attack(atkType, defType):
    # 타입 상성에 따른 데미지 계수 설정
    effectiveness = {
        '노말': {'노말': 1, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 1, '격투': 1, '독': 1, '땅': 1, '비행': 1, '에스퍼': 1, '벌레': 1, '바위': 0.5, '고스트': 0, '드래곤': 1, '악': 1, '강철': 0.5},
        '불': {'노말': 1, '불': 0.5, '물': 0.5, '풀': 2, '전기': 1, '얼음': 2, '격투': 1, '독': 1, '땅': 1, '비행': 1, '에스퍼': 1, '벌레': 2, '바위': 0.5, '고스트': 1, '드래곤': 0.5, '악': 1, '강철': 2},
        '물': {'노말': 1, '불': 2, '물': 0.5, '풀': 0.5, '전기': 1, '얼음': 1, '격투': 1, '독': 1, '땅': 2, '비행': 1, '에스퍼': 1, '벌레': 1, '바위': 2, '고스트': 1, '드래곤': 0.5, '악': 1, '강철': 1},
        '풀': {'노말': 1, '불': 0.5, '물': 2, '풀': 0.5, '전기': 1, '얼음': 1, '격투': 1, '독': 0.5, '땅': 2, '비행': 0.5, '에스퍼': 1, '벌레': 0.5, '바위': 2, '고스트': 1, '드래곤': 0.5, '악': 1, '강철': 0.5},
        '전기': {'노말': 1, '불': 1, '물': 2, '풀': 0.5, '전기': 0.5, '얼음': 1, '격투': 1, '독': 1, '땅': 0, '비행': 2, '에스퍼': 1, '벌레': 1, '바위': 1, '고스트': 1, '드래곤': 0.5, '악': 1, '강철': 1},
        '얼음': {'노말': 1, '불': 0.5, '물': 0.5, '풀': 2, '전기': 1, '얼음': 0.5, '격투': 1, '독': 1, '땅': 2, '비행': 2, '에스퍼': 1, '벌레': 1, '바위': 1, '고스트': 1, '드래곤': 2, '악': 1, '강철': 0.5},
        '격투': {'노말': 2, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 2, '격투': 1, '독': 0.5, '땅': 1, '비행': 0.5, '에스퍼': 0.5, '벌레': 0.5, '바위': 2, '고스트': 0, '드래곤': 1, '악': 2, '강철': 2},
        '독': {'노말': 1, '불': 1, '물': 1, '풀': 2, '전기': 1, '얼음': 1, '격투': 1, '독': 0.5, '땅': 0.5, '비행': 1, '에스퍼': 1, '벌레': 1, '바위': 0.5, '고스트': 0.5, '드래곤': 1, '악': 1, '강철': 0},
        '땅': {'노말': 1, '불': 2, '물': 1, '풀': 0.5, '전기': 2, '얼음': 1, '격투': 1, '독': 2, '땅': 1, '비행': 0, '에스퍼': 1, '벌레': 0.5, '바위': 2, '고스트': 1, '드래곤': 1, '악': 1, '강철': 2},
        '비행': {'노말': 1, '불': 1, '물': 1, '풀': 2, '전기': 0.5, '얼음': 1, '격투': 2, '독': 1, '땅': 1, '비행': 1, '에스퍼': 1, '벌레': 2, '바위': 0.5, '고스트': 1, '드래곤': 1, '악': 1, '강철': 0.5},
        '에스퍼': {'노말': 1, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 1, '격투': 2, '독': 2, '땅': 1, '비행': 1, '에스퍼': 0.5, '벌레': 1, '바위': 1, '고스트': 1, '드래곤': 1, '악': 0, '강철': 0.5},
        '벌레': {'노말': 1, '불': 0.5, '물': 1, '풀': 2, '전기': 1, '얼음': 1, '격투': 0.5, '독': 0.5, '땅': 1, '비행': 0.5, '에스퍼': 2, '벌레': 1, '바위': 2, '고스트': 0.5, '드래곤': 1, '악': 2, '강철': 0.5},
        '바위': {'노말': 1, '불': 2, '물': 1, '풀': 1, '전기': 1, '얼음': 2, '격투': 0.5, '독': 1, '땅': 0.5, '비행': 2, '에스퍼': 1, '벌레': 2, '바위': 1, '고스트': 1, '드래곤': 1, '악': 1, '강철': 0.5},
        '고스트': {'노말': 0, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 1, '격투': 1, '독': 1, '땅': 1, '비행': 1, '에스퍼': 2, '벌레': 1, '바위': 1, '고스트': 2, '드래곤': 1, '악': 0.5, '강철': 1},
        '드래곤': {'노말': 1, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 1, '격투': 1, '독': 1, '땅': 1, '비행': 1, '에스퍼': 1, '벌레': 1, '바위': 1, '고스트': 1, '드래곤': 2, '악': 1, '강철': 0.5},
        '악': {'노말': 1, '불': 1, '물': 1, '풀': 1, '전기': 1, '얼음': 1, '격투': 0.5, '독': 1, '땅': 1, '비행': 1, '에스퍼': 2, '벌레': 1, '바위': 1, '고스트': 2, '드래곤': 1, '악': 0.5, '강철': 1},
        '강철': {'노말': 1, '불': 0.5, '물': 0.5, '풀': 1, '전기': 0.5, '얼음': 2, '격투': 1, '독': 1, '땅': 1, '비행': 1, '에스퍼': 1, '벌레': 1, '바위': 2, '고스트': 1, '드래곤': 1, '악': 1, '강철': 0.5}
    }

    eff = effectiveness[atkType][defType]
    return eff

def damageCal(lv, sk_mul, eff):
    dam = 5 + 145*sk_mul/5 * 1.7
    final_damage = dam * eff * lv/100
    return int(final_damage)

def damageDec(eff):
    if eff==2:
        print("""
    효과가 굉장했다!""")
    elif eff==0.5:
        print("""
    효과가 별로인듯 하다""")
    elif eff==0:
        print("""
    효과가 없는 것 같다...""")

PockemonType = ['노말', '불', '물', '풀', '전기', '얼음', '격투', '독', '땅', '비행', '에스퍼', '벌레', '바위',
                '고스트', '드래곤', '악', '강철']
PkmSrtList = ['이상해씨', '파이리', '꼬부기', '피카츄']
PockemonStarting = {'이상해씨':[5,'풀'], '파이리':[5,'풀'], '꼬부기':[5,'풀'], '피카츄':[5,'전기']}
PockemonEv1 = {'이상해풀':[25,'풀'], '리자드':[25,'풀'], '어니부기':[25,'풀']}
PockemonEv2 = ['이상해꽃', '리자몽', '거북왕']
PockemonLev1 = {'캐터피' : [2, '벌레'], '구구':[3,'비행'], '뿔충이':[6,'벌레'] , '꼬렛':[8, '노말']}
PockemonLev2 = {'니드런' : [8,'독'] , '모래두지': [11, '땅'] , '아보':[13,'독'], '깨비참' : [9,'비행']}
PockemonLev3 = {'파라스' : [13,'물'], '골뱃' : [17,'비행'], '고라파덕' : [14,'물'], '우츠동' : [18,'풀']}
PockemonLev4 = {'찌리리공':[20,'전기'],'텅구리':[24,'땅'],'시드라':[29,'물'], '폴리곤':[28,'노말']}
PockemonLev5 = {'레어코일':[30,'강철'], '롱스톤':[31,'바위'], '날쌩마':[38,'불'],'아쿠스타':[36,'물']}
PockemonLev6 = {'강챙이':[42,'물'],'시라소몬':[46,'격투'], '홍수몬':[46,'격투'], '또도가스':[44,'독']}
PockemonLev7 = {'마그마':[50,'불'], '에레브':[50,'전기'], '쁘사이저':[54,'벌레'],'팬텀':[58,'고스트'],'투구푸스':[57,'바위']}
PockemonLev8 = {'프테라' : [60,'비행'], '괴력몬':[69,'격투'],'후딘':[63,'에스퍼'],'코뿌리' : [68,'땅'], '나인테일': [64,'불']}
PockemonLev9 = {'프리져' : [76,'얼음'], '썬더' : [77,'전기'], '파이어' : [78,'불']}
PockemonLev10 = {'라프라스': [84,'얼음'], '갸라도스' : [88,'물'], '켄타우로스' : [81,'노말'], '망나뇽' : [91,'드래곤']}
PockemonFinal = {'뮤츠': [100,'에스퍼']}
PockemonChampion = {'역상성' : [92,'역타입'], '나시' : [81,'풀'], '갸랴도스' : [84,'비행'], '후딘' : [85,'에스퍼'], '마기라스' : [88,'악'], '윈디' : [90,'불'] }
PockemonRed = {'피카츄' : [100,'전기'], '잠만보' : [96,'노말'], '라프라스': [94,'얼음'], '이상해꽃' : [97,'풀'], '거북왕': [98,'물'], '리자몽' : [99,'불']}
PockemonList = [PockemonStarting, PockemonEv1,
                PockemonLev1,
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
flying_skill,psychic_skill,ground_skill,bug_skill,rock_skill,ghost_skill,dragon_skill,evil_skill,stell_skill]

damage = dict()
for sk in skills:
    for i, skill in enumerate(sk):
        damage[skill] = i+1

skill_type = dict(zip(PockemonType, skills))
print(skill_type)
print(damage)

locations = ['태초마을', '1번도로', '상록시티', '8번도로', '회색시티', '20번 수로', '블루시티', '17번도로', '갈색시티',
             '보라타운', '4번도로', '무지개시티', '16번도로', '연분홍시티', '사파리존', '노랑시티', '28번도로', '홍련마을', '14번도로',
             '석영고원', '23번도로', '포켓몬리그', '동성폭포', '이름없는동굴', '28번도로', '은빛산', '은빛산 정상']
def checkPkmName(pkm):
    if (pkm in PkmSrtList):
        return pkm
    elif pkm.isdigit():
        if (int(pkm)-1) >= 0 and (int(pkm)-1) < len(PkmSrtList):
            return PkmSrtList[int(pkm)-1]
    else:
        return False
def findPkm(num):
    if num == 1:
        return

# Settings
# for pkmDict in PockemonList:
#     for pkm in pkmDict:
#         Type(pkm, pkmDict[pkm][1])
#     #Type(pkm.keys(), list(pkm.values())[1])



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
    Pkm = Pockemon(checkPkmName(startPkm))
    myPkm = MyMon(Pkm.name)
    myPkm.setInfo(PockemonStarting[myPkm.name])
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
locIdx = 0
loc = locations[locIdx]
isOver = False
isWin = False
#PockemonChampion['역상성'][1] = Type(myPkm.rivalMon())
PockemonChampion[MyMon.rivalMon(myPkm)] = PockemonChampion.pop('역상성')

act = 0
while True:
    print("=" * 150)
    print(f"\n현재 위치 : {loc}\n")

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
        loc = Chr.move(locations)
        print('')
        print("="*150)
        print(f"\n현재 위치 : {loc}")
        nowWild = Pockemon(random.choice([i for i in PkmChoice(locIdx)]))
        nowWild.setInfo(PkmChoice(locIdx)[nowWild.name])
        print(f"""
    야생의 {nowWild.name}(Lv.{nowWild.getLevel()}) 이/가 나타났다!
    가라 {myPkm.name}!
        """)
        toDo = int(input('무엇을 할까?\n'
                         '1. 전투\n'
                         '2. 도망친다\n'
                         '숫자를 입력하세요 : '))

        if toDo==1:
            battleBegin()
            print('\n사용 가능한 기술')
            mySkills = myPkm.getSkills(myPkm.getType())
            enSkills = nowWild.getSkills(nowWild.getType())
            print(f"{'\n'.join([str(idx+1)+ ") " + i for idx, i in enumerate(mySkills)])}")

            while True:
                mySkill = random.choice(mySkills)
                print(f"""
    {myPkm.name} 는(은) {mySkill}를 사용했다! """)
                damageDec(attack(myPkm.getType(), nowWild.getType()))
                nowWild.hpCon(damageCal(myPkm.getLevel(), damage[mySkill], attack(myPkm.getType(), nowWild.getType())))
                if (isOver):
                    isWin = 1
                    break

                enSkill = random.choice(enSkills)
                print(f"""
        적 {nowWild.name} 는(은) {enSkill}를 사용했다! """)
                damageDec(attack(nowWild.getType(), myPkm.getType()))
                myPkm.hpCon(damageCal(nowWild.getLevel(), damage[enSkill], attack(nowWild.getType(), myPkm.getType())))
                if (isOver):
                    break
            if isWin == 1:
                myPkm.lvUp()
                locIdx += 1
                print("레벨업!")
            else:
                locIdx -= 1
                print(f"""
    {Chr.name}은 눈 앞이 깜깜해졌다...
    서둘러 포켓몬센터로 돌아가자...""")

            myPkm.restore(PockemonStarting[myPkm.name])

        else:
            Chr.run(myPkm.getLevel(), nowWild.getLevel())
    elif act==2:
        if myPkm.getLevel() > 10:
            Chr.move(locations)
            print(f"""
    {loc}에 도착했다!""")
        else:
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