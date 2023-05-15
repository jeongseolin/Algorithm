def solution(money):
    answer = []
    coffee = money // 5500
    last_money = money % 5500
    answer = [coffee, last_money]
    return answer