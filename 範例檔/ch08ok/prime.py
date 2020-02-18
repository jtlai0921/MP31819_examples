import math
def is_prime(n):
    i=2
    while i<=math.sqrt(n):
        if n % i == 0:  # 如果整除,i是n的因數,回傳False
            return False
        i=i+1
    return True

n = int(input('請輸入一個數字: '))  
if is_prime(n):
    print(n,'是質數')
else:
    print(n,'不是質數')
