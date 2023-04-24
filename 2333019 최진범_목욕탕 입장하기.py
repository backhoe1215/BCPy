gender = input("성별을 입력하세요 (남자: 'm', 여자: 'w'): ")
age = int(input("나이를 입력하세요: "))

if age < 5:
    print("아무탕이나 입장!")
elif gender == 'm':
    print("남탕으로 입장!")
elif gender == 'w':
    print("여탕으로 입장!")
else:
    print("!!잘못된 입력!!")
