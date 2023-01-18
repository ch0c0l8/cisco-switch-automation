'''
텔넷으로 스위치에 접속하여
sh run 실행 후 결과값을 저장하는 프로그램
'''
import telnetlib

ips = ['192.168.0.1', '192.168.0.2', '192.168.0.3']

for ip in ips:
    test = telnetlib.Telnet(ip,'23')
    print(ip + " 텔넷 접속 완료")

    test.read_until(b"Username: ")
    print(ip + " 아이디 입력 기다리는 중")
    test.write('nextit'.encode('utf-8') + b'\n') 
    print(ip + " 아이디 입력 완료")

    test.read_until(b"Password: ")
    print(ip + " 비밀번호 입력 기다리는 중")
    test.write('sprtmxm_01'.encode('utf-8') + b'\n')
    print(ip + " 비밀번호 입력 완료")

    test.write(b'en\n')
    test.write(b'sprtmxm_01\n')
    test.write(b'sh run\n')
    test.write(b' ' * 10 + b'\n')
    print(ip + " 명령어 입력 완료")
    test.write(b'exit\n')
    print(ip + " 텔넷 연결 종료")

    with open(ip + '_result.txt', 'w') as f:
        f.write(test.read_all().decode('utf-8'))
    print(ip + " 출력 완료")
