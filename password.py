password = '0704'
pw_input = '0000'
while pw_input != password:
    pw_input = input('암호를 입력하세요:')
    if pw_input != password:
        print('암호가 틀렸습니다. 다시 입력해주세요.')
print('문이 열렸습니다.')