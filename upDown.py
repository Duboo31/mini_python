import random

# 1 ~ 100 숫자 생성
random_number = random.randint(1, 100)

# 유저 입력값
user_input = 0

# 카운트
cnt = 0


# 재시작 함수
def restart_game():
    print("게임을 다시 하겠?")
    while True:
        global cnt
        cnt = 0
        global random_number
        random_number = random.randint(1, 100)

        y_or_n = input("다시 시작 : y or n :")
        if y_or_n == "y" or y_or_n == "Y":
            return True
        elif y_or_n == "n" or y_or_n == "N":
            return False
        else:
            print("y or n 입력")


print("-- 업 다운 게임 시작 --")

while True:
    try:
        user_input = int(input("입력 : "))

        if user_input > 100 or user_input < 1:
            print("1 ~ 100 사이의 숫자만 입력하세요")
        elif user_input < random_number:
            cnt += 1
            print(f"{user_input} 보다 큼")
        elif user_input > random_number:
            cnt += 1
            print(f"{user_input} 보다 작음")
        else:
            cnt += 1
            print(f"정답 - 시도횟수 : {cnt}")
            if restart_game():
                continue
            else:
                break
    except:
        print("숫자만 입력가능")

# -------------------------------------------------------------------------------------------------------
# - input을 이용해서 사용자의 입력을 받을 수 있는가? ㅇ
# - input으로 받은 값을 string에서 int로 바꿀 수 있는가? ㅇ
# - while문을 사용하고 특정조건에서 break를 걸어서 멈출 수 있는가? ㅇ
# - if문을 이용해서 조건에 따른 코드 실행을 바꿀 수 있는가? ㅇ

# 1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요. ㅇ
# 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요. ㅇ
# 3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요. ??? X
