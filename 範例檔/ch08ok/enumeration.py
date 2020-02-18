num=1000
i=1
while True:
    num=num-i   
    if num<0:
        break
    i=i+1
print(num)
print('依枚舉法得知,一直到淢到數字',i,',相減的結果開始為負數')
