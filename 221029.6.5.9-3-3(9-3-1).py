coffee = 0

def coffee_machine(button):
    print()
    print("#1.뜨거운 물을 준비한다.");
    print("#2.종이컵을 준비한다.");

    if coffee == 1:
        print("#3.아메리카노를 탄다")
    elif coffee==2:
        print("#3.카페라떼를 탄다")
    elif coffee==3:
        print("#3.카푸치노를 탄다")
    elif coffee==4:
        print("#3.에스프로소를 탄다\n")

    print("#4.물을 붓는다");
    print("#5.스푼으로 저어서 녹인다");     
    print()

coffee=int(input("소진손님은 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프로소)"))
coffee_machine(coffee)
print("소진손님~ 커피 여기 있습니다.\n");

coffee=int(input("유라손님은 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프로소)"))
coffee_machine(coffee)
print("유라손님~ 커피 여기 있습니다.\n");

coffee=int(input("민아손님은 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프로소)"))
coffee_machine(coffee)
print("민아손님~ 커피 여기 있습니다.\n");

coffee=int(input("혜리손님은 어떤 커피 드릴까요?(1:아메리카노,2:카페라떼,3:카푸치노,4:에스프로소)"))
coffee_machine(coffee)
print("혜리손님~ 커피 여기 있습니다.\n");