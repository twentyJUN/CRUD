user = []

def print_menu():
    print(" [0] 프로그램 종료\n [1] 회원 정보 입력\n [2] 회원 정보 검색\n [3] 회원 정보 수정\n [4] 회원 정보 삭제\n [5] 회원 목록 보기\n")

print("CRUD 쇼핑몰입니다\n");

while True:
    print_menu()
    menu = int(input("원하시는 번호를 입력해 주세요 : "))
    print("-------------------------------------")
    if menu == 0:
        print("프로그램을 종료 합니다")
        break
    
    elif menu == 1:
        print(" 1.  회원 정보 입력을 선택하셨습니다\n")
        name = input("입력하실 회원님의 성함을 입력해주세요 : ")
        user.append(name)
        print("-------------------------------------")
        
    elif menu == 2:
        print(" 2.  회원 정보 검색을 선택하셨습니다\n")
        name = input("검색하실 성함을 입력해주세요 : ")
        serch = [i for i in user if name in i]
        print(serch)
        print("-------------------------------------")
    elif menu == 3:
        print(" 3.  회원 정보 수정을 선택하셨습니다\n")
        for index, value in enumerate(user):
            print(index, value)
        number = int(input("수정하실 회원 번호를 입력해주세요 : "))
        modify = input("수정할 회원 이름을 작성해주세요 : ")
        user[number] = modify
        print("수정 되었습니다 ^^\n")
        print("-------------------------------------")

    elif menu == 4:
        print(" 4.  회원 정보 삭제를 선택하셨습니다\n")
        for index, value in enumerate(user):
            print(index, value)
        number = int(input("삭제하실 회원 번호를 입력해주세요 : "))
        del user[number]
        print("삭제 되었습니다 ^^\n")
        print("-------------------------------------")


    elif menu == 5:
        print(user)
        print("-------------------------------------")
        
        
    else:
        print("잘못된 번호를 입력하셨습니다")
