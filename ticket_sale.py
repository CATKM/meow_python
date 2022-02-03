age = int(input('당신의 나이는?:'))

if age < 20:
    print('입장권이 20% 할인됩니다.')
elif age >= 65:
    print('입장권이 50% 할인됩니다.')
else:
    print('입장권 할인이 없습니다.')