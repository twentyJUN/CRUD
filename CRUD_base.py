user = []

def print_menu():
    print(" [1] 회원 정보 입력\n [2] 회원 정보 검색\n [3] 회원 정보 검색\n [4]회원 정보 삭제\n")

print("CRUD 쇼핑몰입니다\n");

while True:
    print_menu()
    menu = int(input("원하시는 번호를 입력해 주세요 : "))
    if menu == 1:
        print(" [1] 회원 정보 입력을 선택하셨습니다\n")
        name = input("회원님의 성함을 입력해주세요 : ")
        user.append(name)
        select = input("회원 정보를 더 추가하시겠습니까? y/n : ")
        if select == 'n':
            break;
            
        elif select == 'y':
            name = input("회원님의 성함을 입력해주세요 : ")
            user.append(name)
            break;
            
    elif menu == 2:
        print("[2] 회원 정보 검색을 선택하셨습니다\n")
    
    elif menu == 3:
        print("[3] 회원 정보 수정을 선택하셨습니다\n")
        
    elif menu == 4:
        print("[4] 회원 정보 삭제를 선택하셨습니다\n")
        
    else:
        print("잘못된 번호를 입력하셨습니다")
