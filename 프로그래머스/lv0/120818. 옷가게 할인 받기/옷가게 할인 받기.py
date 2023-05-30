def solution(price):
    discount = 0 

    if price >= 500000:  
        discount = 0.2
    elif price >= 300000: 
        discount = 0.1
    elif price >= 100000:  
        discount = 0.05

    discounted_price = price - (price * discount)
    total_price = int(discounted_price)

    return total_price