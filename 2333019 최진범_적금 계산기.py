monthly_savings = int(input("매월 저축하실 금액을 입력하세요: "))
interest_rate = 0.0025
goal = 100000000

savings = 0
months = 0
years = 0

while savings < goal:
    months += 1
    savings += monthly_savings
    savings *= (1 + interest_rate)
    if months % 12 == 0:
        years += 1

print(f"{years}년 {months % 12}개월 걸렸습니다.")
