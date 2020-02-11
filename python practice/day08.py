# if ~ elif 문
# elif는 if문을 사용할 때 여러개의 조건식을 사용하고 싶을 때 쓰는 문법입니다
# if문의 조건식이 거짓일 경우 elif의 조건식을 비교합니다
# elif의 조건식에서 결과가 참이면 더이상 그 아래에 있는 문장은 실행하지 않습니다
# (elif의 조건식에서 결과가 참이면 그 아래에 있는 같은조건식 문장은 실행됩니다)
# elif는 독립적으로 사용할 수 없습니다 반드시 if와 같이 사용합니다
# elif조건식 뒤에 else사용 가능합니다
# 순서, 조건식의 범위설정 중요

# num = int(input("정수를 입력하세요 : "))
# if num > 0 :
#     print("정수는 양수입니다")
# elif num == 0 :
#     print("정수는 0입니다")
# elif num == 0 :
#     print("정수는 0입니다")
# elif num < 0 :
#     print("정수는 음수입니다")
# else :
#     print("다시 입력하세요")

# 사용자에게 점수를 입력받아서 90점 이상이면 A
# 80점이상 89점 이하 B
# 70점이상 79점 이하 C
# 60점이상 69점 이하 D
# 나머지 F 출력
# 소스코드에 반드시 논리 연산자를 한번은 사용해야 합니다

# scr = int(input("점수를 입력하세요 : "))
# if scr >= 90 :
#     print("A입니다")
# elif scr >= 80 and scr <= 89 :
#     print("B입니다")
# elif scr >= 70 and scr <= 79 :
#     print("C입니다")
# elif scr >= 60 and scr <= 69 :
#     print("D입니다")
# else :
#     print("F입니다")

# while 반복문
# while 문은 if 와 동일하게 조건식을 사용합니다
# 조건식의 결과가 참이면 while의 종속문장을 실행하고
# 거짓이면 실행하지 않습니다
# while 종속문자을 모두 실행하면 다시 자신의 조건식으로 돌아와서
# 조건식을 다시 비교 합니다
# 조건식의 결과가 계속 참이면 반복문을 종료 할 수 없고 그런 형태를 무한루프 라고 합니다
# 사용형식
# while 조건식 :
#     종속문장1:
#     종속문장2: 
# print종료시킬려면 ctrl c 

# a = 0
# while a == 0:
#     print("hello")

# a = 1
# while a < 11 :
#     print("박수를 %d번 쳤습니다"%a)
#     a = a + 1

# 기본적으로 사과가 10개가 있습니다
# 반복문을 사용해서 사과의 갯수를 0을 만들어주세요
# 출력문구는 사과는 ?개 남았습니다
#apple = 10
#while apple > -1 :
    #print("사과는 %d개 남았습니다"%apple)
    #apple = apple - 1
    #apple -= 1 #같은 결과가 나온다

# a = 10
# while a :
#     print("사과는 %d개 남았습니다"%a)
#     a = a - 1
#조건문에 0을 입력하면 거짓으로 판단
# while 0 :
#     print("Hello")

# 사용자에게 구구단 단수를 입력받아서 해당하는 구구단만
# 출력할 수 있는 프로그램을 만들어 주세요
# 사용자는 반드시 2~9까지 숫자만 입력해야 합니다
# 다른 숫자를 입력하면 "잘못된 값 입니다 다시입력하세요" 라는 문구가 나와야 합니다
# 그리고 구구단 출력이 끝나면 다시 단수를 입력받는 문구가 실행이 되여야 합니다


# while True :
#     num1 = int(input("정수를 입력하세요 : "))
#     if 2 <= num1 <= 9 :
#         num2 = 1
#         while num2 <= 9 :
#             print("{}X{}={}".format(num1,num2,num1*num2))
#             num2 = num2 + 1  #블록처리 후 tap키를 누르면 자동으로 들여쓰기가 됩니다
#     else :
#         print("잘못된 값 입니다 다시입력하세요")