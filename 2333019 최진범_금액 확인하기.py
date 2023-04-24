unit_kum = [100000000, 10000, 1000, 100, 10, 1]  # 단위 금액 리스트
unit_won = ['억', '만', '천', '백', '십', '']  # 단위 금액 명칭 리스트
outwon = ''  # 출력될 문자열
unit_len = len(unit_kum)

for i in range(unit_len):
    out = str(unit_kum[i]) + ' : ' + unit_won[i]  # 숫자를 문자열로 변경, 문자열 연결
    print(out)

inwon = int(input(">금액 입력(천억 단위 이하 숫자로)? "))  # 숫자 금액

for i in range(unit_len):
    if inwon // unit_kum[i] > 0:
        outwon += str(inwon // unit_kum[i]) + unit_won[i]
        inwon = inwon % unit_kum[i]
    if inwon == 0:
        break

outwon += '원'

print('>> ' + outwon)
