from turtle import *

print('4: 정사각형, 5: 정오각형, 6: 정육각형')
select = int(input('그리고자 하는 도형의 번호를 입력하세요:'))

if select == 4:
    for a in range(4):
        forward(100)
        right(90)
elif select == 5:
    for a in range(5):
        forward(100)
        right(72)
elif select == 6:
    for a in range(6):
        forward(100)
        right(60)
else:
    print('잘못 입력하셨습니다.')