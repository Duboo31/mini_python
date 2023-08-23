import random

random_num = random.randrange(0, 3)

RSP = ["가위", "바위", "보"]

# 승 패 부 카운트
score = {"win_cnt": 0, "lose_cnt": 0, "tie_cnt": 0}

WIN, LOSE, TIE = [0, 1, 2]


# 재시작 함수
def restart_game():
    print("게임을 다시 하겠?")
    while True:
        y_or_n = input("다시 시작 : y(ㅇㅋ) or n(ㄴ) :")
        if y_or_n == "y" or y_or_n == "Y" or y_or_n == "ㅇㅋ":
            return True
        elif y_or_n == "n" or y_or_n == "N" or y_or_n == "ㄴ":
            print(
                f"승 : {score['win_cnt']}\n패 : {score['lose_cnt']}\n무 : {score['tie_cnt']}"
            )
            return False
        else:
            print("y or n 입력")


def check_result(user, comp):
    if not user in RSP:
        print("가위 바위 보 중에 입력하세요")
        return False

    if user == comp:
        score["tie_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 무")
    elif user == RSP[0] and comp == RSP[1]:
        score["lose_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 패")
    elif user == RSP[0] and comp == RSP[2]:
        score["win_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 승")
    elif user == RSP[1] and comp == RSP[0]:
        score["win_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 승")
    elif user == RSP[1] and comp == RSP[2]:
        score["lose_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 패")
    elif user == RSP[2] and comp == RSP[0]:
        score["lose_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 패")
    elif user == RSP[2] and comp == RSP[1]:
        score["win_cnt"] += 1
        print(f"유저 : {user} - 컴터 : {comp} : 승")

    return True


print("-- 가위 바위 보 게임 시작 --")
while True:
    user_input = input("가위, 바위, 보 입력 : ")
    com_output = RSP[random_num]

    if check_result(user_input, com_output) and restart_game():
        continue
    else:
        break


# -------------------------------------------------------------------------------------------------------
# 1. 플레이어와 컴퓨터가 참여하는 가위바위보 게임을 만드세요.
# 2. 게임은 다음 순서로 진행됩니다.
#     - 플레이어가 가위, 바위, 보 중 하나를 입력합니다. ㅇ
#     - 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다. ㅇ
#     - 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다. ㅇ
#     - 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다. ㅇ
#     - 게임을 반복하거나 종료할 수 있는 기능을 추가하세요. ㅇ


# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요. ㅇ
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요. ??
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요. ㅇ


# - 사용자의 입력값을 ‘가위 바위 보’로 제한할 수 있는가 ㅇ
# - 컴퓨터가 랜덤으로 ‘가위 바위 보’를 선택하게 할 수 있는가 ㅇ
# - 다중 if 문으로 승패를 비교할 수 있는가 ㅇ
# - while문을 이용해서 경기롤 반복시키고 통계를 만들 수 있는가 ㅇ
